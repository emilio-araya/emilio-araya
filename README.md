# Emilio Araya

**Backend · Java + Spring Boot** — estudiante de Ingeniería en Informática, Chile.

> Busco mi primera posición backend: práctica o junior, remoto o en Santiago.

Profundizando en concurrencia y transacciones, IAM y networking en AWS, y seguridad de APIs.

## Pedidos360

Plataforma de pedidos: SPA React, un BFF y dos microservicios Spring Boot sobre Oracle.

| Componente | Responsabilidad | Tests | Cobertura |
|---|---|---|---|
| [`catalog`](https://github.com/emilio-araya/pedidos360-catalog) | Catálogo y reservas de stock | 30 | 84.3% |
| [`orders`](https://github.com/emilio-araya/pedidos360-orders) | Pedidos y liberación de stock | 49 | — |
| [`bff`](https://github.com/emilio-araya/pedidos360-bff) | Entrada única e identidad | 30 | — |
| [`frontend`](https://github.com/emilio-araya/pedidos360-frontend) | SPA React + Vite + TypeScript | 66 | 78.6% |
| [`infra`](https://github.com/emilio-araya/pedidos360-infra) | Terraform en AWS | — | — |

JWT de Entra ID y Cognito · reservas idempotentes con locks pesimistas · Flyway

<sub>![catalog](https://github.com/emilio-araya/pedidos360-catalog/actions/workflows/ci.yml/badge.svg?style=flat-square&label=catalog) ![orders](https://github.com/emilio-araya/pedidos360-orders/actions/workflows/ci.yml/badge.svg?style=flat-square&label=orders) ![bff](https://github.com/emilio-araya/pedidos360-bff/actions/workflows/ci.yml/badge.svg?style=flat-square&label=bff) ![frontend](https://github.com/emilio-araya/pedidos360-frontend/actions/workflows/ci.yml/badge.svg?style=flat-square&label=frontend) ![ecomarket](https://github.com/emilio-araya/ecomarket-spa/actions/workflows/ci.yml/badge.svg?style=flat-square&label=ecomarket)</sub>

### Tres decisiones

- **La paginación rechaza, no recorta.** Un `size` fuera de rango devuelve `400 INVALID_PAGINATION` en vez de aplicar un límite invisible, y el orden se fija por nombre e id para que dos páginas no se solapen.
- **La reserva de stock es idempotente y no deja huérfanos.** Se libera stock incluso si el pedido ya no existe: consistencia antes que disponibilidad.
- **El build de release exige configuración real.** Sin variables de entorno falla, en vez de publicar un bundle apuntando a `localhost`.

## Otros proyectos

- **[Ecomarket](https://github.com/emilio-araya/ecomarket-spa)** — API REST por capas con Spring Boot, JPA y MariaDB. 21 tests y CI contra MariaDB.
- **[Alerta de temperaturas](https://github.com/emilio-araya/caso1-alerta-temperaturas)** — app Android en Kotlin y Compose, con MVVM y DataStore. 24 archivos de test.
- **[Innovatech](https://github.com/emilio-araya/proyecto-innovatech)** — pipeline de GitHub Actions a ECR y EKS, Docker y Kubernetes. Proyecto en equipo.

Trabajos de curso: [PL/SQL sobre Oracle](https://github.com/emilio-araya/programacion-bases-datos-plsql) · [Arduino](https://github.com/emilio-araya/riego-automatico-arduino).

## Stack

**Backend** — Spring Boot · Spring Security (JWT) · JPA / Hibernate · Maven

**Datos** — Oracle (PL/SQL) · MariaDB · Flyway

**Frontend** — React · Vite

**Infraestructura** — Docker · Kubernetes (manifiestos y EKS) · AWS (Terraform, ECR, S3, CloudFront) · GitHub Actions

**Testing** — JUnit 5 · Mockito · Vitest

## Contacto

[LinkedIn](https://www.linkedin.com/in/emilio-araya-213621253) · [emilio.araya.dev@gmail.com](mailto:emilio.araya.dev@gmail.com)
