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

User Input → A1 → A2 → A3 → A6 → A4 → Final Output

1. User submits natural language system description  
2. A1 extracts structured requirements  
3. A2 generates code artefacts and architecture  
4. A3 validates outputs against requirements  
5. A6 evaluates deployment readiness  
6. A4 aggregates results into a final structured output  

---

## Example Output

The system produces structured JSON outputs including:

- Requirements specification
- Code artefacts and project structure
- Validation reports
- Deployment configuration
- Traceability mappings

---

## Repository Structure

agentic-sdlc-framework/

├── workflows/ # Agent workflow definitions (A1–A6)
├── outputs/ # Example outputs from agents
├── diagrams/ # System architecture and BPMN diagrams
├── dashboard/ # Dashboard interface (UI layer)
├── evaluation/ # Execution results and performance data
├── deployment/ # Deployment configurations and evidence
└── README.md

---

## Technologies Used

- Python (system integration)
- n8n (workflow orchestration)
- OpenAI API (LLM-based reasoning and generation)
- JSON (structured data exchange)
- Flask (generated backend applications)

---

## How to Run

> Note: This is a research prototype demonstrating SDLC automation.

1. Set up n8n workflows (A1–A6)
2. Configure API access (OpenAI)
3. Trigger the orchestration workflow (A4)
4. Submit a natural language system description
5. Receive structured SDLC output

---

## Evaluation

The framework was evaluated across multiple case study scenarios:

- Student Helpdesk System  
- Healthcare Appointment System  
- Library Management System  

### Key Findings

- Strong performance in requirements structuring and traceability  
- Consistent generation of system architecture  
- Effective validation of requirement coverage  
- Limited implementation depth (scaffold-level systems)  

---

## Limitations

- Generated systems are not fully production-ready  
- Limited business logic implementation  
- No integrated automated testing  
- Security features (e.g., authentication) are incomplete  
- Output quality depends on prompt design  

---

## Future Work

- Deeper code generation and full implementation support  
- Integration of automated testing frameworks  
- Enhanced security and compliance features  
- Iterative feedback loops between agents  
- Support for additional SDLC stages  
- Multi-language and full-stack support  

---

## Dissertation Context

This project was developed as part of a final-year BSc Computer Science dissertation:

**"An Agentic AI Framework for Automating the Software Development Lifecycle"**

The work explores the feasibility of using multi-agent AI systems to enable structured, end-to-end automation of the SDLC.

---

## Author

Murtaza Ali  
BSc Computer Science  
University of Derby  

---

## License

This project is licensed under the MIT License.
