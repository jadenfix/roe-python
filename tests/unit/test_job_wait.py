from types import SimpleNamespace

import pytest

from roe.models import job as job_module
from roe.models.job import Job, JobBatch, JobStatus


class FakeClock:
    def __init__(self):
        self.now = 0.0

    def monotonic(self):
        return self.now

    def sleep(self, seconds):
        self.now += seconds


@pytest.fixture
def clock(monkeypatch):
    fake = FakeClock()
    monkeypatch.setattr(job_module, "time", fake)
    return fake


def test_job_wait_does_not_sleep_past_timeout(clock):
    jobs = SimpleNamespace(
        retrieve_status=lambda job_id: SimpleNamespace(
            status=JobStatus.STARTED, error_message=None
        )
    )
    job = Job(SimpleNamespace(jobs=jobs), "job-1")

    with pytest.raises(TimeoutError):
        job.wait(interval=60, timeout=1)

    assert clock.now == 1


def test_job_batch_wait_does_not_sleep_past_timeout(clock):
    jobs = SimpleNamespace(
        retrieve_status_many=lambda job_ids: [
            {"id": job_id, "status": JobStatus.STARTED} for job_id in job_ids
        ]
    )
    batch = JobBatch(SimpleNamespace(jobs=jobs), ["job-1"])

    with pytest.raises(TimeoutError):
        batch.wait(interval=60, timeout=1)

    assert clock.now == 1
