from _typeshed import Incomplete, Self
from collections.abc import Callable
from threading import Lock
from typing import Any, ClassVar, Generic, overload
from types import TracebackType

from redis.client import PubSub, Redis
from redis.commands import RedisClusterCommands, CommandsParser
from redis.commands.core import _StrType
from redis.connection import BaseParser, Encoder
from redis.exceptions import RedisError
from redis.connection import Connection, Encoder

def get_node_name(host: str, port: int) -> str: ...
def get_connection(redis_node: Redis, *args, **options) -> Connection: ...
def parse_scan_result(command, res, **options): ...
def parse_pubsub_numsub(command, res, **options): ...
def parse_cluster_slots(resp, **options): ...

PRIMARY: str
REPLICA: str
SLOT_ID: str
REDIS_ALLOWED_KEYS: tuple[str, ...]
KWARGS_DISABLED_KEYS: tuple[str, ...]

def cleanup_kwargs(**kwargs): ...

# It uses `DefaultParser` in real life, but it is a dynamic base class.
class ClusterParser(BaseParser): ...

class AbstractRedisCluster:
    RedisClusterRequestTTL: ClassVar[int]
    PRIMARIES: ClassVar[str]
    REPLICAS: ClassVar[str]
    ALL_NODES: ClassVar[str]
    RANDOM: ClassVar[str]
    DEFAULT_NODE: ClassVar[str]
    NODE_FLAGS: ClassVar[set[str]]
    COMMAND_FLAGS: ClassVar[dict[str, str]]
    CLUSTER_COMMANDS_RESPONSE_CALLBACKS: ClassVar[dict[str, Any]]
    RESULT_CALLBACKS: ClassVar[dict[str, Any]]
    ERRORS_ALLOW_RETRY: ClassVar[tuple[type[RedisError], ...]]

class RedisCluster(AbstractRedisCluster, RedisClusterCommands[_StrType], Generic[_StrType]):
    user_on_connect_func: Callable[[Connection], object]
    encoder: Encoder
    cluster_error_retry_attempts: int
    command_flags: dict[str, str]
    node_flags: set[str]
    read_from_replicas: bool
    reinitialize_counter: int
    reinitialize_steps: int
    nodes_manager: NodesManager
    cluster_response_callbacks: dict[str, Any]
    result_callbacks: dict[str, Any]
    commands_parser: CommandsParser
    @overload
    def __init__(
        self,
        url: str,
        host: None = ...,
        port: None = ...,
        startup_nodes: list[ClusterNode] | None = ...,
        cluster_error_retry_attempts: int = ...,
        require_full_coverage: bool = ...,
        reinitialize_steps: int = ...,
        read_from_replicas: bool = ...,
        dynamic_startup_nodes: bool = ...,
        **kwargs,
    ) -> None: ...
    @overload
    def __init__(
        self,
        host: str,
        port: int = ...,
        startup_nodes: list[ClusterNode] | None = ...,
        cluster_error_retry_attempts: int = ...,
        require_full_coverage: bool = ...,
        reinitialize_steps: int = ...,
        read_from_replicas: bool = ...,
        dynamic_startup_nodes: bool = ...,
        url: None = ...,
        **kwargs,
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def __del__(self) -> None: ...
    def disconnect_connection_pools(self) -> None: ...
    @classmethod
    def from_url(cls: type[Self], url: str, **kwargs) -> Self: ...
    def on_connect(self, connection) -> None: ...
    def get_redis_connection(self, node): ...
    def get_node(self, host: Any | None = ..., port: Any | None = ..., node_name: Any | None = ...): ...
    def get_primaries(self): ...
    def get_replicas(self): ...
    def get_random_node(self): ...
    def get_nodes(self): ...
    def get_node_from_key(self, key, replica: bool = ...): ...
    def get_default_node(self): ...
    def set_default_node(self, node): ...
    def monitor(self, target_node: Any | None = ...): ...
    def pubsub(self, node: Any | None = ..., host: Any | None = ..., port: Any | None = ..., **kwargs): ...
    def pipeline(self, transaction: Any | None = ..., shard_hint: Any | None = ...): ...
    def lock(
        self,
        name: str,
        timeout: float | None = ...,
        sleep: float = ...,
        blocking: bool = ...,
        blocking_timeout: float | None = ...,
        lock_class: type[Incomplete] | None = ...,
        thread_local: bool = ...,
    ): ...
    def keyslot(self, key): ...
    def determine_slot(self, *args): ...
    def get_encoder(self): ...
    def get_connection_kwargs(self): ...
    def execute_command(self, *args, **kwargs): ...
    def close(self) -> None: ...

class ClusterNode:
    host: Any
    port: Any
    name: Any
    server_type: Any
    redis_connection: Any
    def __init__(self, host, port, server_type: Any | None = ..., redis_connection: Any | None = ...) -> None: ...
    def __eq__(self, obj): ...
    def __del__(self) -> None: ...

class LoadBalancer:
    primary_to_idx: Any
    start_index: Any
    def __init__(self, start_index: int = ...) -> None: ...
    def get_server_index(self, primary, list_size): ...
    def reset(self) -> None: ...

class NodesManager:
    nodes_cache: Any
    slots_cache: Any
    startup_nodes: Any
    default_node: Any
    from_url: Any
    connection_kwargs: Any
    read_load_balancer: Any
    def __init__(
        self,
        startup_nodes,
        from_url: bool = ...,
        require_full_coverage: bool = ...,
        lock: Incomplete | None = ...,
        dynamic_startup_nodes: bool = ...,
        **kwargs,
    ) -> None: ...
    def get_node(self, host: Any | None = ..., port: Any | None = ..., node_name: Any | None = ...): ...
    def update_moved_exception(self, exception) -> None: ...
    def get_node_from_slot(self, slot, read_from_replicas: bool = ..., server_type: Any | None = ...): ...
    def get_nodes_by_server_type(self, server_type): ...
    def populate_startup_nodes(self, nodes) -> None: ...
    def check_slots_coverage(self, slots_cache): ...
    def create_redis_connections(self, nodes) -> None: ...
    def create_redis_node(self, host, port, **kwargs): ...
    def initialize(self) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...

class ClusterPubSub(PubSub):
    node: Any
    cluster: Any
    def __init__(
        self, redis_cluster, node: Any | None = ..., host: Any | None = ..., port: Any | None = ..., **kwargs
    ) -> None: ...
    def set_pubsub_node(self, cluster, node: Any | None = ..., host: Any | None = ..., port: Any | None = ...) -> None: ...
    def get_pubsub_node(self): ...
    def execute_command(self, *args, **kwargs) -> None: ...
    def get_redis_connection(self): ...

class ClusterPipeline(RedisCluster[_StrType], Generic[_StrType]):
    command_stack: list[Incomplete]
    nodes_manager: Incomplete
    refresh_table_asap: bool
    result_callbacks: Incomplete
    startup_nodes: Incomplete
    read_from_replicas: bool
    command_flags: Incomplete
    cluster_response_callbacks: Incomplete
    cluster_error_retry_attempts: int
    reinitialize_counter: int
    reinitialize_steps: int
    encoder: Encoder
    commands_parser: Incomplete
    def __init__(
        self,
        nodes_manager,
        commands_parser,
        result_callbacks: Incomplete | None = ...,
        cluster_response_callbacks: Incomplete | None = ...,
        startup_nodes: Incomplete | None = ...,
        read_from_replicas: bool = ...,
        cluster_error_retry_attempts: int = ...,
        reinitialize_steps: int = ...,
        lock: Lock | None = ...,
        **kwargs,
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __nonzero__(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def execute_command(self, *args, **kwargs): ...
    def pipeline_execute_command(self, *args, **options): ...
    def raise_first_error(self, stack) -> None: ...
    def annotate_exception(self, exception, number, command) -> None: ...
    def execute(self, raise_on_error: bool = ...): ...
    scripts: Any
    watching: bool
    explicit_transaction: bool
    def reset(self) -> None: ...
    def send_cluster_commands(self, stack, raise_on_error: bool = ..., allow_redirections: bool = ...): ...
    def eval(self) -> None: ...
    def multi(self) -> None: ...
    def immediate_execute_command(self, *args, **options) -> None: ...
    def load_scripts(self) -> None: ...
    def watch(self, *names) -> None: ...
    def unwatch(self) -> None: ...
    def script_load_for_pipeline(self, *args, **kwargs) -> None: ...
    def delete(self, *names): ...

def block_pipeline_command(name: str) -> Callable[..., Any]: ...

class PipelineCommand:
    args: Any
    options: Any
    position: Any
    result: Any
    node: Any
    asking: bool
    def __init__(self, args, options: Any | None = ..., position: Any | None = ...) -> None: ...

class NodeCommands:
    parse_response: Any
    connection_pool: Any
    connection: Any
    commands: Any
    def __init__(self, parse_response, connection_pool, connection) -> None: ...
    def append(self, c) -> None: ...
    def write(self) -> None: ...
    def read(self) -> None: ...
