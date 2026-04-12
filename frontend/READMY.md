## Setup
### OpenAPI TypeScript
Install openapi-typescript as a development dependency:
```bash
npm install -D openapi-typescript
```
Generate TypeScript types from the backend OpenAPI schema:
```bash
npx openapi-typescript $BACKEND_URL/openapi.json -o src/types/types.ts
```
The generated types will be saved to:
```bash
src/types/types.ts
```

#### Setup project:
```bash
npm create vite@latest .   (React framework typescript)
npm install tailwindcss @tailwindcss/cli
npm i i18next
npm install @reduxjs/toolkit react-redux
npm install react-router-dom
```
