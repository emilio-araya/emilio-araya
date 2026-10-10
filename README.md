## Hola, soy Emilio Araya 👋

Estudiante de **Ingeniería en Informática** en Chile, orientado al **desarrollo backend**: Java, Spring Boot, bases de datos, seguridad de APIs y AWS.

Me interesa lo que pasa cuando un sistema deja de ser un CRUD: concurrencia, consistencia de datos, autenticación entre servicios e infraestructura reproducible.

---

### 📦 Pedidos360 — plataforma de pedidos con microservicios

Mi proyecto principal. Frontend React, un BFF y dos microservicios Spring Boot sobre Oracle, con infraestructura en Terraform para AWS.

```text
React SPA ──► API Gateway ──► BFF ──┬──► Catalog ──► Oracle
                                    └──► Orders ───► Oracle
```

- **Seguridad:** OAuth2 Resource Server que valida JWT de Microsoft Entra ID y de AWS Cognito (firma, issuer, audience, expiración y `token_use`), con cadenas de seguridad separadas por proveedor, autorización por roles y a nivel de objeto, y propagación del token entre servicios.
- **Datos:** reservas de stock idempotentes con locks pesimistas para evitar la doble reserva, y migraciones con Flyway.
- **Calidad:** JUnit 5, Mockito y MockMvc, tests de integración y de concurrencia, cobertura mínima con JaCoCo y CI en GitHub Actions.
- **Infraestructura:** Terraform (VPC, ECS Fargate, API Gateway, ALB, RDS Oracle, Secrets Manager, CloudFront) y GitHub Actions con OIDC hacia AWS.

[infra](https://github.com/emilio-araya/pedidos360-infra) · [bff](https://github.com/emilio-araya/pedidos360-bff) · [catalog](https://github.com/emilio-araya/pedidos360-catalog) · [orders](https://github.com/emilio-araya/pedidos360-orders) · [frontend](https://github.com/emilio-araya/pedidos360-frontend)

### 🌡️ [Alerta de temperaturas](https://github.com/emilio-araya/caso1-alerta-temperaturas) — app Android

App en Kotlin y Jetpack Compose para alertar sobre altas temperaturas en galpones. MVVM, Room, WorkManager para el monitoreo en segundo plano, notificaciones y tests de ViewModels.

### ☸️ [Innovatech](https://github.com/emilio-araya/proyecto-innovatech) — microservicios en Amazon EKS

Proyecto en equipo. Hice el pipeline de GitHub Actions que construye las imágenes, las publica en ECR y despliega en EKS, además de los Dockerfiles multi-stage y los manifiestos de Kubernetes.

### 🌱 [Ecomarket](https://github.com/emilio-araya/ecomarket-spa) — API REST

API por capas con Spring Boot, JPA y MariaDB, con validación, manejo global de errores, OpenAPI y tests que corren en CI contra MariaDB.

---

### 🛠️ Stack

**Backend:** Java · Spring Boot · Spring Security · JPA/Hibernate · Maven
**Datos:** Oracle (SQL y PL/SQL) · MariaDB · Flyway
**Cloud y DevOps:** AWS · Terraform · Docker · Kubernetes · GitHub Actions · Linux
**Frontend y móvil:** React · TypeScript · Vite · Kotlin
**Testing:** JUnit 5 · Mockito · Vitest

### 📫 Contacto

[LinkedIn](https://www.linkedin.com/in/emilio-araya-213621253) · [emiliolokillo611@gmail.com](mailto:emiliolokillo611@gmail.com)
