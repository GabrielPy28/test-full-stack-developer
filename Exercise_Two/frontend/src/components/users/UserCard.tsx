import React from 'react';

interface UserCardProps {
	user: any;
}

const UserCard: React.FC<UserCardProps> = ({ user }) => {
	return (
		<div className="card border-dark mb-3">
			<div className="card-body">
				<h5 className="card-title">{user.name}</h5>
				<h6 className="card-subtitle mb-2 text-muted">{user.email}</h6>
				<p className="card-text">
					<strong>Address:</strong> {user.address.street}, {user.address.suite}, {user.address.city},{' '}
					{user.address.zipcode}
				</p>
				<p className="card-text">
					<strong>Geo:</strong> {user.address.geo.lat}, {user.address.geo.lng}
				</p>
			</div>
		</div>
	);
};

export default UserCard;
