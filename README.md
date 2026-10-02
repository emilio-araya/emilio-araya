<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1b27,100:1f6feb&height=180&section=header&text=Emilio%20Araya&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=32&desc=Backend%20Developer%20%C2%B7%20Java%20%C2%B7%20Spring%20Boot%20%C2%B7%20AWS&descAlignY=52&descSize=17" width="100%"/>

<h3 align="center">Estudiante de Ingeniería en Informática · Backend Developer · Chile 🇨🇱</h3>

<p align="center">
  <b>🇬🇧 EN:</b> Computer Engineering student focused on backend development with Java &amp; Spring Boot,
  cloud infrastructure on AWS, and CI/CD automation. Featured projects below 👇
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

---

## 👨‍💻 Sobre mí

Estudiante de Ingeniería en Informática, enfocado en el desarrollo backend y la arquitectura de aplicaciones.

Diseño y desarrollo sistemas backend con Java y Spring Boot, e infraestructura cloud en AWS con Terraform: microservicios, seguridad OAuth2/JWT y automatización CI/CD, con pruebas automatizadas como parte del flujo de desarrollo.

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

---

## 🛠️ Tecnologías y herramientas

### Lenguajes

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)

### Backend y Frontend

![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFC?style=for-the-badge&logo=vite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

### Bases de datos

![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Flyway](https://img.shields.io/badge/Flyway-CC0200?style=for-the-badge&logo=flyway&logoColor=white)

### DevOps y herramientas

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### Testing

![JUnit 5](https://img.shields.io/badge/JUnit_5-25A162?style=for-the-badge&logo=junit5&logoColor=white)
![Mockito](https://img.shields.io/badge/Mockito-78A641?style=for-the-badge)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=for-the-badge&logo=vitest&logoColor=white)

### Hardware

![Arduino](https://img.shields.io/badge/Arduino-00878F?style=for-the-badge&logo=arduino&logoColor=white)

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
  Abierto a colaborar en proyectos de backend y cloud.<br/>
  Si mi perfil te interesa, escríbeme por <a href="https://www.linkedin.com/in/emilio-araya-213621253">LinkedIn</a> o <a href="mailto:emiliolokillo611@gmail.com">correo</a> — respondo rápido.
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,100:1a1b27&height=120&section=footer" width="100%"/>
