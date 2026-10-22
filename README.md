# Emilio Araya

**Backend · Java + Spring Boot** — estudiante de Ingeniería en Informática, Chile.

Busco mi primera posición backend: práctica o junior, remoto o en Santiago. Profundizando en concurrencia y transacciones, IAM y networking en AWS, y seguridad de APIs.

[![CI](https://github.com/emilio-araya/pedidos360-catalog/actions/workflows/ci.yml/badge.svg?label=catalog)](https://github.com/emilio-araya/pedidos360-catalog/actions/workflows/ci.yml) [![CI](https://github.com/emilio-araya/pedidos360-orders/actions/workflows/ci.yml/badge.svg?label=orders)](https://github.com/emilio-araya/pedidos360-orders/actions/workflows/ci.yml) [![CI](https://github.com/emilio-araya/pedidos360-bff/actions/workflows/ci.yml/badge.svg?label=bff)](https://github.com/emilio-araya/pedidos360-bff/actions/workflows/ci.yml) [![CI](https://github.com/emilio-araya/pedidos360-frontend/actions/workflows/ci.yml/badge.svg?label=frontend)](https://github.com/emilio-araya/pedidos360-frontend/actions/workflows/ci.yml) [![CI](https://github.com/emilio-araya/ecomarket-spa/actions/workflows/ci.yml/badge.svg?label=ecomarket)](https://github.com/emilio-araya/ecomarket-spa/actions/workflows/ci.yml)

## Pedidos360

Plataforma de pedidos: SPA React, un BFF y dos microservicios Spring Boot sobre Oracle. JWT de Entra ID y Cognito, reservas de stock idempotentes con locks pesimistas, Flyway y Terraform en AWS.

| Componente | Responsabilidad | Evidencia |
|---|---|---|
| `catalog` | Catálogo y reservas de stock | 30 tests · 84.3% líneas |
| `orders` | Pedidos y liberación de stock | 49 tests |
| `bff` | Entrada única e identidad | 30 tests |
| `frontend` | SPA React + Vite + TypeScript | 66 tests · 78.6% líneas |

Repos: [infra](https://github.com/emilio-araya/pedidos360-infra) · [bff](https://github.com/emilio-araya/pedidos360-bff) · [catalog](https://github.com/emilio-araya/pedidos360-catalog) · [orders](https://github.com/emilio-araya/pedidos360-orders) · [frontend](https://github.com/emilio-araya/pedidos360-frontend)

### Decisiones

- **La paginación rechaza, no recorta.** Un `size` fuera de rango devuelve `400 INVALID_PAGINATION` en vez de aplicar un límite invisible, y el orden se fija por nombre e id para que dos páginas no se solapen.
- **La reserva de stock es idempotente y no deja huérfanos.** Se libera stock incluso si el pedido ya no existe: consistencia antes que disponibilidad, como decisión documentada.
- **El build de release exige configuración real.** Sin variables de entorno falla, en vez de publicar un bundle apuntando a `localhost`.

## Otros proyectos

| Proyecto | Qué es | Evidencia |
|---|---|---|
| [Ecomarket](https://github.com/emilio-araya/ecomarket-spa) | API REST por capas, Spring Boot + JPA + MariaDB | 21 tests · CI contra MariaDB |
| [Alerta de temperaturas](https://github.com/emilio-araya/caso1-alerta-temperaturas) | App Android, Kotlin + Compose, MVVM y DataStore | 24 archivos de test |
| [Innovatech](https://github.com/emilio-araya/proyecto-innovatech) | Pipeline GitHub Actions → ECR/EKS, Docker y Kubernetes (equipo) | — |

Trabajos de curso: [PL/SQL sobre Oracle](https://github.com/emilio-araya/programacion-bases-datos-plsql) · [Arduino](https://github.com/emilio-araya/riego-automatico-arduino).

## Stack

| | |
|---|---|
| Lenguajes | Java · TypeScript · SQL · Kotlin |
| Backend | Spring Boot · Spring Security (JWT) · JPA / Hibernate · Maven |
| Bases de datos | Oracle (PL/SQL: funciones, procedimientos, triggers) · MariaDB · Flyway |
| Frontend | React · Vite |
| Infraestructura | Docker · Kubernetes (manifiestos y despliegue a EKS) · AWS (Terraform: ALB y ECS; CI a ECR, S3 y CloudFront) · GitHub Actions |
| Testing | JUnit 5 · Mockito · Vitest |

## Contacto

[LinkedIn](https://www.linkedin.com/in/emilio-araya-213621253) · emilio.araya.dev@gmail.com
