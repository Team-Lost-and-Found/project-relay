# Architecture Overview

## Components
- **Frontend**: React SPA
- **Backend**: FastAPI with REST endpoints
- **Routing Engine**: NLP model that categorizes and escalates tickets
- **Integrations**: External APIs for ticket creation and alerts

## Flow
1. User submits concern
2. Backend classifies using NLP
3. Routed to department based on rules
4. Integration triggers create/update tickets in external systems
