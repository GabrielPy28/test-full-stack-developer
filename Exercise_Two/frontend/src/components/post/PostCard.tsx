import React from 'react';

interface PostCardProps {
	post: {
		id: number;
		title: string;
		body: string;
	};
}

const PostCard: React.FC<PostCardProps> = ({ post }) => {
	return (
		<div className="card text-bg-light border-secondary mb-4" style={{'height':'300px'}}>
			<div className="card-header" style={{
                    'height':'100px', 'display':'flex', 
                    'flexDirection':'column', 'justifyContent':'center', 
                    'textAlign':'center'
                }}
            >
                {post.title}
            </div>
			<div className="card-body" style={{
                    'height':'100px', 'display':'flex', 
                    'flexDirection':'column', 'justifyContent':'center', 
                    'textAlign':'center'}}>
				<p className="card-text">{post.body}</p>
			</div>
		</div>
	);
};

export default PostCard;
