# Agentic SDLC Framework

A multi-agent AI system for automating key stages of the Software Development Lifecycle (SDLC).

---

## Overview

This project presents a workflow-orchestrated agentic framework that transforms natural language requirements into structured software artefacts through coordinated AI agents. The system integrates multiple specialised agents into a unified pipeline, enabling end-to-end automation from requirements analysis to deployment readiness.

The framework demonstrates **process-level SDLC automation**, moving beyond isolated AI tools toward a coordinated, traceable, and structured software engineering workflow.

---

## Key Features

- Multi-agent architecture (A1–A6)
- End-to-end SDLC automation pipeline
- Natural language → structured requirements transformation
- Automated code generation with traceability
- Validation and requirement coverage analysis
- Deployment readiness analysis
- Workflow orchestration using n8n
- Structured JSON-based data exchange across agents

---

## System Architecture

The framework consists of the following agents:

| Agent | Name | Responsibility |
|------|------|----------------|
| A1 | Requirements Analysis | Extracts structured requirements from natural language |
| A2 | Code Generation | Generates system architecture and implementation scaffold |
| A3 | Validation & Review | Evaluates requirement coverage and system completeness |
| A4 | Orchestration (Master Agent) | Coordinates the full SDLC pipeline |
| A5 | Standalone Deployment | Independent deployment evaluation (testing) |
| A6 | Internal Deployment Analysis | Deployment analysis within pipeline |

The agents are coordinated through a workflow orchestration layer using **n8n**, ensuring deterministic execution and structured data flow.

---

## Workflow Pipeline
