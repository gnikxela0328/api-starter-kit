import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { ColorModeContext, useMode } from './theme';
import { CssBaseline, ThemeProvider } from '@mui/material';
import { Routes, Route } from 'react-router-dom';

import Header from './scenes/global/header';
import Home from "./scenes/home";
import Splash from "./scenes/splash";
import UserForm from './scenes/userForm';

function App() {

  let auth = useSelector(state => state.auth);
  let dispatch = useDispatch()
  let user = true

  const [theme, colorMode] = useMode();

  useEffect(() => {

  })

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="App">
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/add" element={<UserForm />} />
          </Routes>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider >
  );
}

export default App;
