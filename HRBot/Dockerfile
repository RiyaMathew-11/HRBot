FROM rasa/rasa-sdk:2.5.0

USER root

COPY actions /actions

WORKDIR /actions
RUN pip install -r requirements.txt

COPY ./actions/entrypoint.sh ./entrypoint.sh
RUN chmod a+x ./entrypoint.sh
USER 1001



