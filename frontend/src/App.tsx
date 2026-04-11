import { Routes, Route } from 'react-router-dom';
import RootLayout from './RootLayout';
import TodoPage from './pages/TodoPage';
import StatisticsPage from './pages/StatisticsPage';
import SettingsPage from './pages/SettingsPage';

function App() {
  return (
    <Routes>
      <Route path="/" element={<RootLayout />}>
        <Route index element={<TodoPage />} />
        <Route path="stats" element={<StatisticsPage />} />
        <Route path="settings" element={<SettingsPage />} />
      </Route>
    </Routes>
  );
}

export default App;