<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1b27,100:1f6feb&height=180&section=header&text=Emilio%20Araya&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=32&desc=Backend%20Engineer%20%C2%B7%20Java%20%C2%B7%20SQL%20%C2%B7%20Cybersecurity%20%C2%B7%20AWS&descAlignY=52&descSize=17" width="100%"/>

<h3 align="center">Ingeniería en Informática · Backend Development · Cloud & Security · Chile 🇨🇱</h3>

<p align="center">
  <b>Java · Spring Boot · SQL · Spring Security · OAuth2/JWT · AWS · React</b>
</p>

<p align="center">
  Backend-focused developer interested in building secure, reliable and maintainable systems,
  with a strong focus on Java, databases, API security and AWS.
</p>

---

## 👨‍💻 Sobre mí

Soy estudiante de Ingeniería en Informática con orientación hacia el **desarrollo backend**, especialmente en **Java, Spring Boot, SQL, ciberseguridad y AWS**.

Me interesa entender no solo cómo implementar una funcionalidad, sino también los problemas que aparecen cuando un sistema debe ser **seguro, consistente y capaz de manejar múltiples componentes y usuarios**.

Actualmente estoy profundizando en:

* ☕ **Java & Spring Boot** — APIs REST, arquitectura por capas, testing y buenas prácticas.
* 🗄️ **SQL & bases de datos** — Oracle, MariaDB, JPA/Hibernate, transacciones, índices y concurrencia.
* 🔐 **Cybersecurity** — Spring Security, OAuth2, JWT, RBAC, autenticación y autorización de APIs.
* ☁️ **AWS** — API Gateway, VPC, IAM, ALB, ECR, ECS/EKS y CloudWatch.
* 🐳 **DevOps** — Docker, Terraform y GitHub Actions.
* ⚛️ **React** — desarrollo frontend para complementar soluciones backend.

Mi objetivo es crecer como **Backend Engineer**, profundizando especialmente en Java, sistemas distribuidos, bases de datos, seguridad y cloud.

---

## 🚀 Proyecto principal

### 📦 Pedidos360 — Plataforma distribuida de gestión de pedidos

**Pedidos360** es el proyecto que mejor representa mi enfoque actual de desarrollo backend.

La plataforma está dividida en varios servicios y repositorios, con un **BFF en Spring Boot**, microservicios para catálogo y pedidos, frontend React e infraestructura como código.

```text
                         ┌──► Catalog Service ──► Oracle
                         │
React SPA ──► API Gateway ──► BFF
                         │
                         └──► Orders Service ──► Oracle
                                  │
                                  └──► Catalog
```

### 🔐 Seguridad

El sistema implementa autenticación y autorización basada en OAuth2/JWT:

* Microsoft Entra ID.
* AWS Cognito.
* Validación de firma, issuer, audience y expiración.
* Validación de `nbf`.
* Validación de `token_use` para tokens de Cognito.
* Autorización basada en roles.
* Propagación controlada del Bearer Token entre servicios.
* Separación de cadenas de seguridad para diferentes proveedores de identidad.
* Sin registro de tokens o credenciales sensibles en logs.

### 🗄️ Persistencia y consistencia

El backend implementa reglas de negocio que van más allá de un CRUD tradicional:

* Gestión de productos y stock.
* Reservas de stock asociadas a `orderId`.
* Operaciones idempotentes.
* Prevención de doble reserva.
* Locks pesimistas para controlar operaciones concurrentes.
* Liberación de reservas.
* Migraciones de base de datos con Flyway.
* Uso de Oracle en el entorno cloud y H2 para desarrollo/testing.

Una de las partes que más me interesa del proyecto es el manejo de **concurrencia e idempotencia**, especialmente en escenarios donde múltiples solicitudes pueden intentar modificar el mismo stock.

### ☁️ Cloud & Infrastructure

La infraestructura se define mediante **Terraform** y contempla una arquitectura AWS con:

* Amazon API Gateway.
* VPC.
* Subredes privadas.
* Application Load Balancer.
* VPC Link.
* Amazon ECR.
* GitHub Actions + OIDC.
* Docker.
* Arquitectura preparada para servicios backend privados.

Parte de la infraestructura AWS ha sido aplicada y validada, mientras que otros componentes dependen de permisos y restricciones del entorno académico/laboratorio.

### 🧪 Calidad y CI/CD

Los servicios incluyen:

* JUnit 5.
* Mockito.
* Spring MockMvc.
* Tests de seguridad.
* Tests de integración.
* JaCoCo.
* GitHub Actions.
* Umbrales mínimos de cobertura.
* Docker multi-stage builds.

### Repositorios

* [Frontend — React](https://github.com/emilio-araya/pedidos360-frontend)
* [BFF — Spring Boot](https://github.com/emilio-araya/pedidos360-bff)
* [Catalog Service](https://github.com/emilio-araya/pedidos360-catalog)
* [Orders Service](https://github.com/emilio-araya/pedidos360-orders)
* [Infrastructure — Terraform/AWS](https://github.com/emilio-araya/pedidos360-infra)

---

## ☁️ Innovatech — Cloud Native & AWS

Proyecto académico orientado a arquitectura cloud-native, microservicios y DevOps sobre AWS.

**Tecnologías principales:**

* Amazon EKS.
* Kubernetes.
* Amazon ECR.
* Docker.
* GitHub Actions.
* VPC.
* Load Balancing.
* CloudWatch.
* AWS Systems Manager.
* STS.
* Auto Scaling.

### 🔐 Seguridad

El proyecto aplica principios de **Zero Trust**:

* Sin acceso administrativo mediante SSH.
* Uso de AWS Systems Manager.
* Credenciales temporales mediante STS.
* Servicios internos mediante Kubernetes `ClusterIP`.
* Backend aislado mediante redes privadas.

[Ver proyecto](https://github.com/emilio-araya/proyecto-innovatech)

---

## 🌱 Ecomarket — REST API

Proyecto enfocado en fundamentos de desarrollo backend con Java y Spring Boot.

* Java 17.
* Spring Boot.
* Spring Data JPA.
* MariaDB.
* Arquitectura por capas.
* DTOs y validación.
* OpenAPI / Swagger.
* Manejo global de excepciones.
* JUnit 5.
* Mockito.

[Ver repositorio](https://github.com/emilio-araya/ecomarket-spa)

---

## 🧠 Áreas de interés

```text
Backend Engineering
├── Java
│   ├── Spring Boot
│   ├── Spring Security
│   ├── REST APIs
│   └── Testing
│
├── Databases
│   ├── SQL
│   ├── Oracle
│   ├── MariaDB
│   ├── JPA / Hibernate
│   ├── Transactions
│   └── Concurrency
│
├── Cybersecurity
│   ├── OAuth2
│   ├── JWT
│   ├── Authentication
│   ├── Authorization
│   ├── RBAC
│   └── API Security
│
└── Cloud
    ├── AWS
    ├── Docker
    ├── Terraform
    ├── GitHub Actions
    └── Kubernetes
```

---

## 🛠️ Tech Stack

### ☕ Backend

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge\&logo=openjdk\&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge\&logo=springboot\&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge\&logo=springsecurity\&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge\&logo=apachemaven\&logoColor=white)

### 🔐 Security

![OAuth2](https://img.shields.io/badge/OAuth2-000000?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge\&logo=jsonwebtokens\&logoColor=white)

### 🗄️ Databases

![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge\&logo=oracle\&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge\&logo=mariadb\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Flyway](https://img.shields.io/badge/Flyway-CC0200?style=for-the-badge\&logo=flyway\&logoColor=white)

### ☁️ Cloud & DevOps

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge\&logo=amazonwebservices\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge\&logo=terraform\&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge\&logo=kubernetes\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge\&logo=githubactions\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)

### ⚛️ Frontend

![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge\&logo=react\&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge\&logo=typescript\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFC?style=for-the-badge\&logo=vite\&logoColor=white)

### 🧪 Testing

![JUnit 5](https://img.shields.io/badge/JUnit_5-25A162?style=for-the-badge\&logo=junit5\&logoColor=white)
![Mockito](https://img.shields.io/badge/Mockito-78A641?style=for-the-badge)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=for-the-badge\&logo=vitest\&logoColor=white)

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=emilio-araya&show_icons=true&theme=tokyonight&hide_border=true" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=emilio-araya&layout=compact&theme=tokyonight&hide_border=true" height="165" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=emilio-araya&theme=tokyonight&hide_border=true" height="165" />
</p>

---

## 📚 Actualmente profundizando

* Java y JVM
* Concurrencia y programación multihilo
* Spring Security
* OAuth2 / OpenID Connect
* SQL y optimización de consultas
* Transacciones y niveles de aislamiento
* Diseño de APIs seguras
* Arquitectura de sistemas distribuidos
* AWS networking e IAM
* Docker y CI/CD

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
  Abierto a oportunidades y colaboración en proyectos de <b>backend, cloud y cybersecurity</b>.
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,100:1a1b27&height=120&section=footer" width="100%"/>
