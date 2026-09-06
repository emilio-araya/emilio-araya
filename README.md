# Emilio Araya
**Estudiante de Ingeniería en Informática — Backend & Cloud/DevOps** · Chile 🇨🇱
<sub>Nombre completo: Emilio Antonio Araya Ordoñez</sub>


Construyo sistemas completos, no solo funcionalidades aisladas: backend con microservicios, infraestructura cloud en AWS/Azure, y seguridad como parte del diseño, no como un extra al final.

📫 [Email](mailto:emiliolokillo611@gmail.com) · [GitHub](https://github.com/emilio-araya)

---

## 📜 Certificaciones

- **Cybersecurity Awareness (CAPC™)** — Certiprof, emitida el 04/06/2026, válida hasta 06/2027 · ID `CLPPRRQPBYY-ZVJGZJHZV-XCWXMYXWYT`
- **Cybersecurity Foundation (CSFPC™)** — Certiprof, emitida el 29/06/2026, válida hasta 06/2029 · ID `JLRRHTRJJHT-WKWCVKKHK-YTRJGYJGRY`
- **Ethical Hacking Professional (CEHPC™)** — Certiprof, emitida el 06/09/2026, válida hasta 09/2029 · ID `CLPPNVBSNPB-ZVVHVGKJG-XCXXMMXHMW`

---

## 🧰 Stack técnico

**Lenguajes:** Java · Python · JavaScript · TypeScript · SQL (Oracle PL/SQL)
**Backend:** Spring Boot (Web, Data JPA, Security) · Node.js
**Cloud:** AWS (EKS, ECR, VPC, CloudWatch, STS, IAM) · Azure (Entra ID)
**DevOps:** Docker · Kubernetes · Terraform · GitHub Actions (CI/CD)
**Identidad/Seguridad:** OAuth 2.0 · OpenID Connect · JWT · modelo Zero Trust · Ethical Hacking
**Sistemas:** Linux (Arch) · Bash

---

## 🚀 Proyectos principales

### ☁️ Innovatech Chile — Plataforma cloud-native en AWS (Zero Trust)
Plataforma de gestión de despachos con arquitectura de microservicios desplegada en **Amazon EKS**, diseñada bajo un modelo de seguridad **Zero Trust**.

- Infraestructura como código con **Terraform**: VPC dedicada (`10.0.0.0/16`), Multi-AZ, subredes públicas/privadas
- **EKS (Kubernetes v1.35)** con nodos Spot para optimizar costos, y **Horizontal Pod Autoscaler** (umbral 50% CPU)
- **Cero acceso SSH**: administración vía AWS Systems Manager, credenciales temporales con STS
- Pipeline CI/CD completo: GitHub Actions → Docker (multi-stage) → Amazon ECR → despliegue en EKS sin downtime
- 3 microservicios (Frontend, Ventas, Despachos) comunicados vía `ClusterIP`, expuestos solo lo necesario con Load Balancer

**Stack:** Java · Spring Boot · Docker · Kubernetes · Terraform · AWS · GitHub Actions
**Repo:** [proyecto-innovatech](https://github.com/emilio-araya/proyecto-innovatech)

### 🏗️ Ecomarket-SPA — Backend de microservicios con Spring Boot
Sistema backend real de 5 microservicios independientes comunicados a través de un API Gateway:

`productos-service` · `compras-service` · `usuarios-service` · `config-server` · `gateway`

Incluye autenticación y autorización con Spring Security, persistencia con JPA, y configuración centralizada — la arquitectura clásica de un sistema distribuido en producción, aplicada a escala de proyecto académico.

**Stack:** Java 17 · Spring Boot 3 · Spring Security · MySQL/H2 · Maven
**Repo:** [ecomarket-spa](https://github.com/emilio-araya/ecomarket-spa)

### 🔐 Desarrollo Cloud Native — Federación de identidad multi-cloud
Implementé el mismo flujo de autenticación **OAuth 2.0 / OpenID Connect** con dos proveedores distintos para entender qué es transferible entre nubes y qué no:

| | Azure (rama `main`) | AWS (rama `aws`) |
|---|---|---|
| Identidad | Microsoft Entra ID | Amazon Cognito |
| Librería | MSAL | react-oidc-context |
| Protocolo | OAuth 2.0 / OIDC | OAuth 2.0 / OIDC |

**Stack:** React · TypeScript · Vite · JWT
**Repo:** [Desarrollo-Cloud-Native](https://github.com/emilio-araya/Desarrollo-Cloud-Native)

---

## 📂 Otros proyectos

- **[Sistema de Riego Automático (Arduino)](https://github.com/emilio-araya/riego-automatico-arduino)** — sistema embebido con lógica de decisión multi-sensor y programación no bloqueante (`millis()`).
- **[Programación de Bases de Datos — PL/SQL](https://github.com/emilio-araya/Programasion-Bases-de-datos-pl-sql)** — cursores, triggers, procedimientos y funciones en Oracle SQL.
- **[Proyecto E-commerce (carrito de compras)](https://github.com/Nicolasdx1/ProyectoFullStack)** — mi aporte: carrito completo con persistencia en `localStorage`. Proyecto de equipo, alojado en cuenta de un compañero.

---

*Actualmente profundizando en Kubernetes, Terraform, arquitecturas Cloud-Native y aplicaciones potenciadas con IA.*
