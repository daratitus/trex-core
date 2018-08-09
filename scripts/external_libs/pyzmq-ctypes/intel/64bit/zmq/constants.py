'''
Based on pyzmq-ctypes and pyzmq
Updated to work with latest ZMQ shared object

https://github.com/zeromq/pyzmq
https://github.com/svpcom/pyzmq-ctypes
'''

IO_THREADS = 1
MAX_SOCKETS = 2
SOCKET_LIMIT = 3
THREAD_PRIORITY = 3
THREAD_SCHED_POLICY = 4
MAX_MSGSZ = 5

PAIR = 0
PUB = 1
SUB = 2
REQ = 3
REP = 4
DEALER = 5
ROUTER = 6
PULL = 7
PUSH = 8
XPUB = 9
XSUB = 10
STREAM = 11

AFFINITY = 4
ROUTING_ID = 5
SUBSCRIBE = 6
UNSUBSCRIBE = 7
RATE = 8
RECOVERY_IVL = 9
SNDBUF = 11
RCVBUF = 12
RCVMORE = 13
FD = 14
EVENTS = 15
TYPE = 16
LINGER = 17
RECONNECT_IVL = 18
BACKLOG = 19
RECONNECT_IVL_MAX = 21
MAXMSGSIZE = 22
SNDHWM = 23
RCVHWM = 24
MULTICAST_HOPS = 25
RCVTIMEO = 27
SNDTIMEO = 28
LAST_ENDPOINT = 32
ROUTER_MANDATORY = 33
TCP_KEEPALIVE = 34
TCP_KEEPALIVE_CNT = 35
TCP_KEEPALIVE_IDLE = 36
TCP_KEEPALIVE_INTVL = 37
IMMEDIATE = 39
XPUB_VERBOSE = 40
ROUTER_RAW = 41
IPV6 = 42
MECHANISM = 43
PLAIN_SERVER = 44
PLAIN_USERNAME = 45
PLAIN_PASSWORD = 46
CURVE_SERVER = 47
CURVE_PUBLICKEY = 48
CURVE_SECRETKEY = 49
CURVE_SERVERKEY = 50
PROBE_ROUTER = 51
REQ_CORRELATE = 52
REQ_RELAXED = 53
CONFLATE = 54
ZAP_DOMAIN = 55
ROUTER_HANDOVER = 56
TOS = 57
CONNECT_ROUTING_ID = 61
GSSAPI_SERVER = 62
GSSAPI_PRINCIPAL = 63
GSSAPI_SERVICE_PRINCIPAL = 64
GSSAPI_PLAINTEXT = 65
HANDSHAKE_IVL = 66
SOCKS_PROXY = 68
XPUB_NODROP = 69
BLOCKY = 70
XPUB_MANUAL = 71
XPUB_WELCOME_MSG = 72
STREAM_NOTIFY = 73
INVERT_MATCHING = 74
HEARTBEAT_IVL = 75
HEARTBEAT_TTL = 76
HEARTBEAT_TIMEOUT = 77
XPUB_VERBOSER = 78
CONNECT_TIMEOUT = 79
TCP_MAXRT = 80
THREAD_SAFE = 81
MULTICAST_MAXTPDU = 84
VMCI_BUFFER_SIZE = 85
VMCI_BUFFER_MIN_SIZE = 86
VMCI_BUFFER_MAX_SIZE = 87
VMCI_CONNECT_TIMEOUT = 88
USE_FD = 89

POLLIN = 1
POLLOUT = 2
POLLERR = 4
POLLPRI = 8

ZMQ_HAUSNUMERO = 156384712
ETERM = ZMQ_HAUSNUMERO + 53

from errno import EINVAL, EAGAIN, EINTR

try:
    from errno import ENOTSUP
except ImportError:
    from errno import EOPNOTSUPP as ENOTSUP # ENOTSUP is missing, use EOPNOTSUPP - it has same value

