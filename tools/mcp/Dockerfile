FROM python:3.12-slim
WORKDIR /app
COPY . /app/financeskills
EXPOSE 8080
ENV PORT=8080
CMD ["python3", "/app/financeskills/tools/mcp/http_server.py"]
