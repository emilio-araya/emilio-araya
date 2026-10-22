# Emilio Araya

Estudiante de **Ingeniería en Informática** en Chile, orientado a **backend**: Java, Spring Boot, bases de datos, seguridad de APIs y AWS.

**Busco mi primera posición backend (Java / Spring Boot): práctica o junior, remoto o en Santiago.**

Actualmente profundizando en concurrencia y transacciones, IAM y networking en AWS, y seguridad de APIs.

[![CI catalog](https://github.com/emilio-araya/pedidos360-catalog/actions/workflows/ci.yml/badge.svg)](https://github.com/emilio-araya/pedidos360-catalog/actions/workflows/ci.yml)
[![CI orders](https://github.com/emilio-araya/pedidos360-orders/actions/workflows/ci.yml/badge.svg)](https://github.com/emilio-araya/pedidos360-orders/actions/workflows/ci.yml)
[![CI bff](https://github.com/emilio-araya/pedidos360-bff/actions/workflows/ci.yml/badge.svg)](https://github.com/emilio-araya/pedidos360-bff/actions/workflows/ci.yml)
[![CI frontend](https://github.com/emilio-araya/pedidos360-frontend/actions/workflows/ci.yml/badge.svg)](https://github.com/emilio-araya/pedidos360-frontend/actions/workflows/ci.yml)
[![CI ecomarket](https://github.com/emilio-araya/ecomarket-spa/actions/workflows/ci.yml/badge.svg)](https://github.com/emilio-araya/ecomarket-spa/actions/workflows/ci.yml)

## Pedidos360

Plataforma de pedidos con frontend React, un BFF y dos microservicios Spring Boot sobre Oracle. Validación de
JWT de Entra ID y Cognito, reservas de stock idempotentes con locks pesimistas, migraciones Flyway, tests de
integración y de concurrencia, e infraestructura en AWS con Terraform.

[infra](https://github.com/emilio-araya/pedidos360-infra) · [bff](https://github.com/emilio-araya/pedidos360-bff) · [catalog](https://github.com/emilio-araya/pedidos360-catalog) · [orders](https://github.com/emilio-araya/pedidos360-orders) · [frontend](https://github.com/emilio-araya/pedidos360-frontend)

| Componente | Responsabilidad | Evidencia |
|---|---|---|
| `catalog` | Catálogo de productos y reservas de stock | 30 tests · 84.3% de líneas |
| `orders` | Pedidos y liberación de stock | 49 tests |
| `bff` | Entrada única, propagación de identidad y de `X-Request-Id` | 30 tests |
| `frontend` | SPA React + Vite + TypeScript | 66 tests · 78.6% de líneas |

## Decisiones de ingeniería

- **La paginación rechaza, no recorta.** Un `size` fuera de rango devuelve `400 INVALID_PAGINATION` en vez de
  aplicar un límite invisible: si el cliente pide 500 y recibe 100 en silencio, cree que pidió otra cosa. El orden
  se fija por nombre e id porque sin un `ORDER BY` determinista dos páginas pueden solaparse o saltear filas.
- **La reserva de stock es idempotente y la cancelación no deja huérfanos.** Se libera stock incluso si el pedido
  ya no existe; priorizo consistencia sobre disponibilidad y lo documento como una decisión, no como un descuido.
- **El build de release exige configuración real.** Sin las variables de entorno falla, en vez de publicar un
  bundle apuntando a `localhost`: que un artefacto compile no significa que sea desplegable.

## Otros proyectos

- **Ecomarket** — API REST por capas con Spring Boot, JPA y MariaDB; 21 tests y CI contra MariaDB real.
- **Alerta de temperaturas** — app Android en Kotlin y Jetpack Compose con MVVM, DataStore, WorkManager y
  notificaciones; 24 archivos de test.
- **Innovatech** (equipo) — pipeline de GitHub Actions hacia ECR y EKS, Dockerfiles multi-stage y manifiestos de
  Kubernetes.
- **Bases de datos (PL/SQL)** y **riego automático (Arduino)** — trabajos de curso, disponibles en el perfil.

## Stack

Java · Spring Boot · Spring Security · JPA / Hibernate · Maven · SQL (Oracle, MariaDB) · Flyway · TypeScript ·
React · Vite · Docker · Kubernetes · Terraform · AWS · GitHub Actions · JUnit 5 · Mockito · Vitest

## Contacto

[LinkedIn](https://www.linkedin.com/in/emilio-araya-213621253) · emilio.araya.dev@gmail.com
