import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PrivateRoute from './utils/PrivateRoute';
import { AuthProvider } from './context/AuthContext';

import Homepage from './views/Homepage';
import Registerpage from './views/Registerpage';
import Loginpage from './views/Loginpage';
import Dashboard from './views/Dashboard';
import Navbar from './views/Navbar';
import BlogPage from './views/BlogPage';
import ExercisePage from './views/ExercisePage';
import ExerciseItem from './components/ExerciseItem'; // Import the new ExerciseItem component

function App() {
  return (
    <Router>
      <AuthProvider>
        <Navbar />
        <Switch>
          <PrivateRoute
            component={Dashboard}
            path="/dashboard"
            exact
          />
          <Route
            component={Loginpage}
            path="/login"
          />
          <Route
            component={Registerpage}
            path="/register"
            exact
          />
          <Route
            component={Homepage}
            path="/"
            exact
          />
          <Route
            component={BlogPage}
            path="/blog"
            exact
          />
          <Route
            component={ExercisePage}
            path="/exercises"
            exact
          />
          <Route
            component={ExerciseItem}
            path="/exercises/:id"
            exact
          />
        </Switch>
      </AuthProvider>
    </Router>
  );
}

export default App;