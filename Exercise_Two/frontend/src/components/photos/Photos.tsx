import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import PhotoCard from './PhotoCard';

const Photos = () => {
	const { user_id } = useParams<{ user_id: string }>();
	const [ photos, setPhotos ] = useState<{ id: number; title: string; url: string; thumbnailUrl: string }[]>([]);

	useEffect(
		() => {
			const fetchPhotos = async () => {
				const response = await axios.get(`http://localhost:8000/photos/${user_id}`);
				setPhotos(response.data);
			};

			fetchPhotos();
		},
		[ user_id ]
	);

	return (
		<div>
			<h1>Photos by User {user_id}</h1>
			<div className="row g-3" style={{'padding':'25px'}}>
				{photos.map((photo) => (
					<div className="col-md-4" key={photo.id}>
						<PhotoCard photo={photo} />
					</div>
				))}
			</div>
		</div>
	);
};

export default Photos;
