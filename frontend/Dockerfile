FROM python
RUN pip install Flask \
    requests
COPY src /workspace
WORKDIR /workspace
ENV FLASK_APP=main.py
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

