import { Outlet, Link } from 'react-router-dom';
import { useAppSelector } from '../store/hooks';
import { useTranslation } from 'react-i18next';

const RootLayout = () => {
  const { t } = useTranslation();
  const isDarkMode = useAppSelector((state) => state.ui.darkMode);

  return (
    <div className={isDarkMode ? 'dark' : ''}>
      <div className="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 transition-colors duration-300">
        
        <nav className="p-4 border-b border-slate-200 dark:border-slate-800 flex justify-between items-center bg-white dark:bg-slate-800">
          <h1 className="font-bold text-xl text-orange-600">PomoTodo</h1>
          <div className="space-x-4">
            <Link title="Tasks" to="/" className="hover:text-orange-500">{t('nav.tasks')}</Link>
            <Link title="Stats" to="/stats" className="hover:text-orange-500">{t('nav.stats')}</Link>
            <Link title="Settings" to="/settings" className="hover:text-orange-500">{t('nav.settings')}</Link>
          </div>
        </nav>
        <main className="max-w-4xl mx-auto p-6">
          <Outlet />
        </main>

        <footer className="fixed bottom-0 w-full p-2 text-center text-xs opacity-50">
          v1.0.0 - Productive Days Ahead
        </footer>
      </div>
    </div>
  );
};

export default RootLayout;