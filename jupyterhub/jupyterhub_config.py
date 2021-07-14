# JupyterHub configuration
import os
import sys

c = get_config()

## Bitbucket authentication
from oauthenticator.bitbucket import BitbucketOAuthenticator
c.JupyterHub.authenticator_class = BitbucketOAuthenticator
c.BitbucketOAuthenticator.oauth_callback_url = 'http://localhost:8000/hub/oauth_callback'
c.BitbucketOAuthenticator.client_id = '9wMGjwRyaPH4t7wCHu'
c.BitbucketOAuthenticator.client_secret = 'uPfdtafj3k8VLFPBY4Zd8naNJEZjFrGU'
c.Authenticator.admin_users = {'ridenhourz'}

## Authentication
# c.JupyterHub.authenticator_class = 'dummy'
# c.DummyAuthenticator.password = 'test123'
# c.Authenticator.admin_users = {'ridenhourz'}

## Enable lab
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## JupyterHub ip and port
c.JupyterHub.hub_ip = os.environ['HUB_IP']

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']

## User data persistence
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

## Resources
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'

## Spawner initialization
c.JupyterHub.init_spawners_timeout = 30

## Services
c.JupyterHub.services = [
    {
        'name': 'idle-culler',
        'admin': True,
        'command': [
            sys.executable,
            '-m', 'jupyterhub_idle_culler',
            '--timeout=3600'
        ],
    }
]