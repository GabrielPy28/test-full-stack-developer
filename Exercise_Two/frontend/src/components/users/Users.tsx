import React, { useEffect, useState } from 'react';
import axios from 'axios';
import UserCard from './UserCard';

const Users = () => {
	const [ users, setUsers ] = useState([]);

	useEffect(() => {
		const fetchUsers = async () => {
			const response = await axios.get('http://localhost:8000/users');
			setUsers(response.data);
		};

		fetchUsers();
	}, []);

	return (
		<div>
			<h1>Users</h1>
			<div className="row g-3" style={{'padding':'25px'}}>
				{users.map((user: any) => (
					<div className="col-md-4" key={user.id}>
						<UserCard user={user} />
					</div>
				))}
			</div>
		</div>
	);
};

export default Users;
