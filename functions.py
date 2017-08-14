import re
import yaml

def yaml_fetcher(file_name):
    with open('{}.yaml'.format(file_name), 'r') as stream:
        return yaml.load(stream)

def is_allowed_user(email):
    domain = yaml_fetcher('config')['domain']
    allowed_domain_pattern = re.compile(r'^\S+@{}$'.format(domain))
    return bool(re.match(allowed_domain_pattern, email))
