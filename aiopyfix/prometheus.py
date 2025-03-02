from prometheus_client import Counter

DROPPED_SEND = Counter('dropped_send', 'Sends dropped due to connection being closed')
