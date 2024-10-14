use actix_web::{get, web, App, HttpServer, HttpRequest, HttpResponse, Responder};
use std::f64;

#[get("/workload/async-sleep")]
async fn async_sleep() -> impl Responder {
    tokio::time::sleep(std::time::Duration::from_secs(1)).await;
    HttpResponse::Ok().body("Async sleep done!")
}

#[get("/workload/prime-number")]
async fn prime_number() -> impl Responder {
    let max_number = 50000;
    let mut primes = Vec::new();

    for n in 3..=max_number {
        let sqrt_n = (n as f64).sqrt() as usize + 1;
        let mut is_prime = true;

        for i in 2..sqrt_n {
            if n % i == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            primes.push(n.to_string());
        }
    }

    HttpResponse::Ok().body(primes.join(","))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(async_sleep)
            .service(prime_number)
    })
    .bind(("0.0.0.0", 8000))?
    .run()
    .await
}