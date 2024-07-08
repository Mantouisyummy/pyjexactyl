from dataclasses import dataclass, fields
from typing import Optional, Dict
from datetime import datetime

from pyjexactyl.api.base import create_environment_dataclass


@dataclass
class LimitsDataclass:
    """
    The limits of the server

    """
    memory: int
    swap: int
    disk: int
    io: int
    cpu: int
    threads: Optional[int]

    @classmethod
    def from_dict(cls, limits_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: limits_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class FeatureLimitsDataclass:
    databases: int
    allocations: int
    backups: int

    @classmethod
    def from_dict(cls, feature_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: feature_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class ContainerDataclass:
    startup_command: str
    image: str
    installed: bool
    environment: dict

    @classmethod
    def from_dict(cls, container_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: container_dict.get(field) for field in field_names}
        return cls(**kwargs)

    def __post_init__(self):
        self.environment = create_environment_dataclass(self.environment)


@dataclass
class ServerDataclass:
    id: int
    external_id: str
    uuid: str
    identifier: str
    name: str
    description: str
    suspended: bool
    limits: LimitsDataclass
    feature_limits: FeatureLimitsDataclass
    user: int
    node: int
    allocation: int
    nest: int
    egg: int
    status: str
    container: ContainerDataclass
    updated_at: str
    created_at: str

    def __post_init__(self):
        self.feature_limits = FeatureLimitsDataclass.from_dict(self.feature_limits)
        self.container = ContainerDataclass.from_dict(self.container)

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class DatabasePassword:
    object: str
    password: str


@dataclass
class DatabaseHost:
    object: str
    id: int
    name: str
    host: str
    port: int
    username: str
    node: int
    created_at: datetime
    updated_at: datetime


@dataclass
class Relationships:
    password: DatabasePassword
    host: DatabaseHost

    def __post_init__(self):
        self.password = DatabasePassword(**self.password)
        self.host = DatabaseHost(**self.host)


@dataclass
class DatabaseListDataclass:
    id: int
    server: int
    host: int
    database: str
    username: str
    remote: str
    max_connections: int
    created_at: datetime
    updated_at: datetime
    relationships: Relationships

    def __post_init__(self):
        self.relationships = Relationships(**self.relationships)

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class DatabaseDataclass:
    id: int
    server: int
    host: int
    database: str
    username: str
    remote: str
    max_connections: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class UserDataclass:
    id: int
    external_id: str
    uuid: str
    username: str
    email: str
    first_name: str
    last_name: str
    language: str
    root_admin: bool
    discord_id: int
    two_factor_auth: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        kwargs['two_factor_auth'] = kwargs.pop('2fa', None)
        return cls(**kwargs)


@dataclass
class AllocationDataclass:
    id: int
    ip: str
    ailas: Optional[str]
    port: int
    notes: Optional[str]
    assigned: bool

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class LocationDataclass:
    id: int
    short: str
    long: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class PterodactylSSL:
    enabled: bool
    cert: str
    key: str


@dataclass
class JexactylAPI:
    host: str
    port: int
    ssl: PterodactylSSL
    upload_limit: int

    def __post_init__(self):
        self.ssl = PterodactylSSL(**self.ssl)


@dataclass
class JexactylSystemSFTP:
    bind_port: int


@dataclass
class JexactylSystem:
    data: str
    sftp: JexactylSystemSFTP

    def __post_init__(self):
        self.sftp = JexactylSystemSFTP(**self.sftp)


@dataclass
class NodeConfiguration:
    debug: bool
    uuid: str
    token_id: str
    token: str
    api: JexactylAPI
    system: JexactylSystem
    remote: str

    def __post_init__(self):
        self.api = JexactylAPI(**self.api)
        self.system = JexactylSystem(**self.system)


@dataclass
class NodeDataclass:
    id: int
    uuid: str
    public: bool
    name: str
    description: str
    location_id: int
    fqdn: str
    scheme: str
    behind_proxy: bool
    maintenance_mode: bool
    memory: int
    memory_overallocate: int
    disk: int
    disk_overallocate: int
    upload_size: int
    daemon_listen: int
    daemon_sftp: int
    daemon_base: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class NestDataclass:
    id: int
    uuid: str
    author: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)


@dataclass
class EggConfig:
    parser: str
    find: Dict[str, Optional[str]]


@dataclass
class EggScript:
    privileged: bool
    install: str
    entry: str
    container: str
    extends: Optional[str]


@dataclass
class EggDataclass:
    id: int
    uuid: str
    name: str
    nest: int
    author: str
    description: str
    docker_image: str
    config: EggConfig
    startup: str
    script: EggScript
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        self.config = EggConfig(**self.config)
        self.script = EggScript(**self.script)

    @classmethod
    def from_dict(cls, user_dict):
        field_names = [field.name for field in fields(cls)]
        kwargs = {field: user_dict.get(field) for field in field_names}
        return cls(**kwargs)
