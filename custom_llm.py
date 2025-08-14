import os
import logging
from typing import List, Any, Optional, Iterator

# --- LangChain Core Components ---
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage, HumanMessage, SystemMessage
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult

# --- OpenAI Client (for OpenRouter) ---
from openai import OpenAI

import config

# --- The Final and Correct OpenRouter Model Implementation ---
class OpenRouterChatModel(BaseChatModel):
    """
    Custom LangChain Chat Model wrapper for the OpenRouter API.
    This class uses the official OpenAI SDK and the exact structure from the reference code.
    """
    model_name: str = config.OPENROUTER_MODEL_NAME
    temperature: float = 0.1
    _client: Optional[OpenAI] = None

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            logging.critical("OPENROUTER_API_KEY environment variable not set.")
            raise ValueError("OPENROUTER_API_KEY environment variable not set.")
        
        # Instantiate the OpenAI client pointing to the OpenRouter base URL
        self._client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

    def _convert_message_to_dict(self, message: BaseMessage) -> dict:
        """Converts a LangChain message to a simple Python dictionary."""
        if isinstance(message, HumanMessage):
            return {"role": "user", "content": message.content}
        elif isinstance(message, AIMessage):
            return {"role": "assistant", "content": message.content}
        elif isinstance(message, SystemMessage):
            return {"role": "system", "content": message.content}
        else:
            raise ValueError(f"Got unknown message type: {message}")

    def _stream(self, messages: List[BaseMessage], stop: Optional[List[str]] = None, **kwargs: Any) -> Iterator[ChatGenerationChunk]:
        """Handles a streaming request to the OpenRouter API."""
        openai_messages = [self._convert_message_to_dict(m) for m in messages]
        
        try:
            stream = self._client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": config.SITE_URL,
                    "X-Title": config.SITE_TITLE,
                },
                model=self.model_name,
                messages=openai_messages,
                temperature=self.temperature,
                stream=True,
                extra_body={},
            )
            
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content is not None:
                    delta_content = chunk.choices[0].delta.content
                    yield ChatGenerationChunk(message=AIMessageChunk(content=delta_content))

        except Exception as e:
            logging.error(f"An error occurred during streaming with the OpenRouter API: {e}", exc_info=True)
            yield ChatGenerationChunk(message=AIMessageChunk(content=f"**Error:** Could not get response from AI model. Details: {e}"))

    def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None, **kwargs: Any) -> ChatResult:
        """
        Handles a non-streaming request to the OpenRouter API, exactly matching the reference.
        """
        # Convert messages to the dictionary format required by the API
        openai_messages = [self._convert_message_to_dict(m) for m in messages]
        
        try:
            # --- Make the API call using the exact structure from your reference ---
            completion = self._client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": config.SITE_URL,
                    "X-Title": config.SITE_TITLE,
                },
                extra_body={}, # Added to match the new reference
                model=self.model_name,
                messages=openai_messages,
                temperature=self.temperature,
            )
            
            # --- Parse the response ---
            response_content = completion.choices[0].message.content
            message = AIMessage(content=response_content)
            return ChatResult(generations=[ChatGeneration(message=message)])

        except Exception as e:
            logging.error(f"An error occurred with the OpenRouter API: {e}")
            error_message = AIMessage(content=f"**Error:** Could not get response from AI model. Please check the logs. Details: {e}")
            return ChatResult(generations=[ChatGeneration(message=error_message)])

    @property
    def _llm_type(self) -> str:
        return "openrouter_chat_model"