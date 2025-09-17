from pydantic import BaseModel, Field


class VideoSchedulerConfig(BaseModel):
    host: str = Field(default="localhost")
    port: int = Field(default=8000)
    max_synthetic_queue_size: int = Field(default=100) 
    refill_target: int = Field(default=10)
    refill_threshold: int = Field(default=9) 
    min_video_len: int = Field(default=29.7)
    max_video_len: int = Field(default=40)
    pexels_max_size: int = Field(default=10)
    pexels_threshold: int = Field(default=9)
    weight_hd_to_4k: float = Field(default=0)
    weight_sd_to_hd: float = Field(default=1)
    weight_sd_to_4k: float = Field(default=0.3)
    weight_4k_to_8k: float = Field(default=0.1)
    weight_hd_to_8k: float = Field(default=0.1)
