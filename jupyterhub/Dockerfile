FROM jupyterhub/jupyterhub:1.4.1

COPY jupyterhub_config.py .

RUN pip install \
    dockerspawner==12.0.0 \
    jupyterhub-idle-culler==1.1 \
    jupyterlab==3.0.16 \
    notebook==6.4.0 \
    oauthenticator==14.0.0