# Mock AI Interview - Frontend

A modern React application for conducting AI-powered mock interviews.

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Copy environment variables:
```bash
cp env.example .env
```

3. Update the `.env` file with your API endpoints and configuration.

4. Start the development server:
```bash
npm start
```

The app will open at [http://localhost:3000](http://localhost:3000)

## 📦 Available Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run lint` - Check code quality
- `npm run lint:fix` - Fix linting issues
- `npm run format` - Format code with Prettier

## 🛠 Tech Stack

- **React 18** - Modern React with hooks
- **TypeScript** - Type safety and better DX
- **Material-UI** - Beautiful, accessible UI components
- **Redux Toolkit** - Efficient state management
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **Socket.IO** - Real-time communication
- **React Webcam** - Camera integration for interviews
- **Styled Components** - CSS-in-JS styling

## 📁 Project Structure

```
src/
├── components/     # Reusable UI components
├── pages/         # Page components
├── hooks/         # Custom React hooks
├── services/      # API services and utilities
├── types/         # TypeScript type definitions
├── utils/         # Helper functions
├── assets/        # Static assets (images, icons)
└── styles/        # Global styles and themes
```

## 🔗 API Integration

The frontend is configured to work with:
- **API Gateway**: `http://localhost:8000/api`
- **AI Service**: `http://localhost:8001`
- **WebSocket**: `ws://localhost:8000/ws`

## 🎨 Features

- Modern, responsive UI with Material-UI
- Real-time interview sessions with WebSocket
- Video recording with webcam integration
- State management with Redux Toolkit
- TypeScript for type safety
- ESLint + Prettier for code quality
- Path aliases for clean imports

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

- `REACT_APP_API_BASE_URL` - Backend API URL
- `REACT_APP_AI_SERVICE_URL` - AI service URL
- `REACT_APP_WS_URL` - WebSocket URL
- `REACT_APP_ENABLE_WEBCAM` - Enable/disable webcam features
- `REACT_APP_ENABLE_AUDIO_RECORDING` - Enable/disable audio recording

### Path Aliases

The project supports clean imports with path aliases:

```typescript
import Button from '@/components/Button';
import { useInterview } from '@/hooks/useInterview';
import { InterviewService } from '@/services/InterviewService';
```

## 📱 Development

### Code Style
- ESLint for code quality
- Prettier for formatting
- TypeScript strict mode enabled
- Pre-configured rules for React best practices

### Testing
- Jest and React Testing Library configured
- Run tests with `npm test`

## 🚀 Deployment

Build for production:
```bash
npm run build
```

The `build` folder contains the optimized production build.

## 🤝 Contributing

1. Follow the ESLint and Prettier configurations
2. Write tests for new features
3. Use TypeScript for type safety
4. Follow the established folder structure 