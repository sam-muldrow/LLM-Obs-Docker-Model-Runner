# A Simple LLM App that uses Docker Model Runner and Datadog LLM Obs

This chatbot uses [The LLM Obs SDK for Python](https://docs.datadoghq.com/llm_observability/instrumentation/), and also the [OpenAI SDK](https://github.com/openai/openai-python/tree/main)

## Quick Start

## Environment Variables

1. Create an `.env` file in the `llm_obs_docker_model_runner` directory with the following:
- `LLM_BASE_URL`: The base URL of the LLM API
- `LLM_MODEL_NAME`: The model name to use. [Here's the list of LLM Models](https://hub.docker.com/u/ai)
- `DD_API_KEY`: A valid datadog API key

2. Enable the [Docker Model Runner](https://docs.docker.com/ai/model-runner/get-started/)

2. Run the application using the script:
   ```bash
   ./run.sh
   ```

3. Open your browser and visit the following links:
   http://localhost:8081 to view the app

4. View the LLM Spans in Datadog
