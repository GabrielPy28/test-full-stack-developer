import React from 'react';

interface PhotoCardProps {
	photo: {
		id: number;
		title: string;
		url: string;
		thumbnailUrl: string;
	};
}

const PhotoCard: React.FC<PhotoCardProps> = ({ photo }) => {
	return (
		<div className="card">
			<img src={photo.url} className="card-img-top" alt={photo.title} />
			<div className="card-body" style={{
                    'height':'90px', 'display':'flex', 
                    'flexDirection':'column', 'justifyContent':'center', 
                    'textAlign':'center'}}>
				<p className="card-text">{photo.title}</p>
			</div>
		</div>
	);
};

export default PhotoCard;
