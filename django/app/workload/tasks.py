from celery import shared_task  # type: ignore
import asyncio
import math

@shared_task()
def hello_world():
    print("start hello_world")
    print("hello")
    print("-----" * 200)
    print("end hello_world")


@shared_task()
def calc(a: int, b: int) -> int:
    result: int = a + b
    return result

@shared_task()
async def celery_sleep():
    await asyncio.sleep(1)

@shared_task()
async def celery_prime_number():
    max_number = 50000
    primes =[]
    for n in range(3, max_number + 1):
        for i in range(2, int(math.sqrt(n) +1)):
            if (n % i) == 0:
                break
        else:
            primes.append(str(n))

    print("prime numbers: ", ",".join(primes))