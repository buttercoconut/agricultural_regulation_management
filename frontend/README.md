# Agricultural Regulation Management System - Frontend

## Project Structure

```
frontend/
├─ src/
│  ├─ components/
│  │  ├─ RegulationList.vue
│  ├─ App.vue
│  ├─ main.js
├─ index.html
```

## Setup

```bash
# Install dependencies
npm install

# Run dev server
npm run dev
```

## Build

```bash
npm run build
```

## Notes

- API base URL is set via `VUE_APP_API_BASE_URL` environment variable or defaults to `http://localhost:8000/api`.
- The `RegulationList` component fetches regulations from `/regulations` endpoint.
- Basic styling is included in the component.
