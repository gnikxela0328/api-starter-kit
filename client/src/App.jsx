import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { ColorModeContext, useMode } from './theme';
import { CssBaseline, ThemeProvider } from '@mui/material';

import Home from "./scenes/home/home";
import Splash from "./scenes/splash/splash";
import Header from './scenes/global/header';

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
          <section>
            {user ? <Home /> : <Splash />}
          </section>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider >
  );
}

export default App;
