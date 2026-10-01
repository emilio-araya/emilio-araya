<h1 align="center">Hola, soy Emilio Araya 👋</h1>

<h3 align="center">Estudiante de Ingeniería en Informática · Backend Developer · Chile 🇨🇱</h3>

<p align="center">
  <b>🇬🇧 EN:</b> Computer Engineering student focused on backend development with Java &amp; Spring Boot,
  cloud infrastructure on AWS, and CI/CD automation. Featured projects below 👇
</p>

---

## 👨‍💻 Sobre mí

Estudiante de Ingeniería en Informática, enfocado en el desarrollo backend y la arquitectura de aplicaciones.

Me gusta construir soluciones modulares, seguras y escalables, aplicando buenas prácticas de programación y herramientas modernas de desarrollo.

**En qué estoy enfocado actualmente:**

* Desarrollo backend con Java y Spring Boot.
* Diseño e integración de APIs REST, con autenticación OAuth2 y JWT.
* Arquitectura de microservicios y diseño de sistemas escalables.
* Infraestructura como código (Terraform) y despliegue en AWS.
* Contenedores, Kubernetes y automatización CI/CD.

---

## 🚀 Proyectos destacados

<p align="center">
  <a href="https://github.com/emilio-araya/pedidos360-frontend">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=emilio-araya&repo=pedidos360-frontend&theme=tokyonight&hide_border=true" />
  </a>
  <a href="https://github.com/emilio-araya/pedidos360-infra">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=emilio-araya&repo=pedidos360-infra&theme=tokyonight&hide_border=true" />
  </a>
  <a href="https://github.com/emilio-araya/proyecto-innovatech">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=emilio-araya&repo=proyecto-innovatech&theme=tokyonight&hide_border=true" />
  </a>
  <a href="https://github.com/emilio-araya/ecomarket-spa">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=emilio-araya&repo=ecomarket-spa&theme=tokyonight&hide_border=true" />
  </a>
</p>

### 📦 Pedidos360 — Plataforma de gestión de pedidos y catálogo

Sistema distribuido compuesto por 5 repositorios: frontend SPA, dos microservicios de negocio, un BFF y la infraestructura como código.

```text
React SPA (MSAL / Amplify) ──► BFF ──► ms-catalog ──► Oracle DB
                                └──► ms-orders  ──► Oracle DB (Flyway)

Auth:  Entra ID (local) · AWS Cognito (nube) — OAuth2 + JWT
AWS:   API Gateway · CloudFront · ECS Fargate · RDS Oracle · Secrets Manager
CI/CD: GitHub Actions + OIDC · Terraform · Docker
```

* Arquitectura de microservicios (catálogo y pedidos) detrás de un BFF en Spring Boot.
* Autenticación OAuth2/JWT dual: Microsoft Entra ID en local y AWS Cognito en la nube.
* Autorización por roles y a nivel de objeto, con propagación de tokens JWT entre servicios.
* Migraciones de base de datos versionadas con Flyway.
* Infraestructura como código con Terraform: API Gateway, CloudFront, ECS Fargate con autoescalado, RDS Oracle y Secrets Manager.
* CI/CD con GitHub Actions: cobertura con JaCoCo y Vitest, y despliegue a AWS vía OIDC (sin credenciales estáticas).

**Repositorios:** [Frontend](https://github.com/emilio-araya/pedidos360-frontend) · [BFF](https://github.com/emilio-araya/pedidos360-bff) · [Catálogo](https://github.com/emilio-araya/pedidos360-catalog) · [Pedidos](https://github.com/emilio-araya/pedidos360-orders) · [Infraestructura](https://github.com/emilio-araya/pedidos360-infra)

---

### ☁️ Innovatech — Infraestructura cloud-native en AWS

Despliegue de microservicios sobre Amazon EKS con prácticas DevOps y modelo de seguridad Zero Trust.

* Arquitectura Multi-AZ con subredes públicas y privadas; backend aislado de internet.
* Pipeline CI/CD: GitHub Actions → Docker (multi-stage build) → ECR → EKS.
* Zero Trust: acceso administrativo sin SSH, mediante AWS Systems Manager y credenciales temporales (STS).
* Autoescalado del clúster y observabilidad centralizada con CloudWatch.

[Ver repositorio](https://github.com/emilio-araya/proyecto-innovatech)

---

### 🌱 Ecomarket — API REST para gestión de productos

Backend en Java 17 / Spring Boot 3 con arquitectura por capas para un sistema de productos ecológicos.

* CRUD completo de productos y proveedores, con validación mediante DTOs.
* Persistencia con Spring Data JPA y MariaDB; respuestas hipermedia con Spring HATEOAS.
* Documentación interactiva de la API con OpenAPI / Swagger UI.
* Manejo centralizado de errores y pruebas con JUnit 5 y Mockito.

[Ver repositorio](https://github.com/emilio-araya/ecomarket-spa)

---

### 🔧 Otros proyectos

* 🌿 **[Riego automático con Arduino](https://github.com/emilio-araya/riego-automatico-arduino)** — Sistema en C++ que controla una bomba de agua según sensores de humedad, lluvia, luminosidad y temperatura.
* 🗄️ **[Bases de datos PL/SQL](https://github.com/emilio-araya/programacion-bases-datos-plsql)** — Prácticas en Oracle: cursores, triggers, funciones, procedimientos, packages y SQL dinámico.
* 📱 **[Aplicaciones Móviles](https://github.com/emilio-araya/Aplicaciones-Moviles)** — Aprendizaje de Kotlin aplicado al desarrollo Android.

---

## 🛠️ Tecnologías y herramientas

### Lenguajes

<p>
  <img src="https://skillicons.dev/icons?i=java,ts,js,html,css" />
</p>

### Backend y Frontend

<p>
  <img src="https://skillicons.dev/icons?i=spring,react,vite" />
</p>

### Bases de datos

<p>
  <img src="https://skillicons.dev/icons?i=mysql,oracle" />
</p>

### DevOps y herramientas

<p>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,aws,terraform,githubactions,maven,nginx,linux,git" />
</p>

### Hardware y otros

<p>
  <img src="https://skillicons.dev/icons?i=arduino,cpp" />
</p>

---

## 📊 Estadísticas de GitHub

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=emilio-araya&show_icons=true&theme=tokyonight&hide_border=true" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=emilio-araya&layout=compact&theme=tokyonight&hide_border=true" height="165" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=emilio-araya&theme=tokyonight&hide_border=true" height="165" />
</p>

---

## 📫 Contacto

<p align="center">
  <a href="https://www.linkedin.com/in/emilio-araya-213621253">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:emiliolokillo611@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://github.com/emilio-araya">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

<p align="center">
  Siempre estoy interesado en aprender nuevas tecnologías y participar en proyectos que me permitan seguir creciendo como desarrollador.
</p>
