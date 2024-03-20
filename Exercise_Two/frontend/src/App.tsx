import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Users from './components/users/Users';
import Posts from './components/post/Posts';
import Photos from './components/photos/Photos';
import Logs from './components/logs/Logs';

const App = () => {
	return (
		<Router>
			<div className="App">
				<nav className="navbar navbar-expand-lg navbar-light bg-light">
					<a className="navbar-brand" href="/">
						Home
					</a>
					<a className="navbar-brand" href="/logs">
						Logs
					</a>
				</nav>

				<Routes>
					<Route path="/users/:user_id">
						<Route index element={<Posts />} />
						<Route path="photos" element={<Photos />} />
					</Route>
					<Route path="/users" element={<Users />} />
					<Route path="/logs" element={<Logs />}>
            {/* Empty Route component to force Logs component re-render */}
          </Route>
					<Route path="/" element={<Users />} />
				</Routes>
			</div>
		</Router>
	);
};

export default App;
