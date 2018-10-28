FROM python
RUN pip install Flask \
    scikit-learn
COPY src /workspace
WORKDIR /workspace
ENV FLASK_APP=predict.py
EXPOSE 8081
CMD ["flask", "run", "--host=0.0.0.0", "--port=8081"]

