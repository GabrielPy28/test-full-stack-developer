import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import PostCard from './PostCard';

const Posts = () => {
	const { user_id } = useParams<{ user_id: string }>();
	const [posts, setPosts] = useState<{ id: number; title: string; body: string }[]>(
		[]
	);

	useEffect(
		() => {
			const fetchPosts = async () => {
				const response = await axios.get(`http://localhost:8000/post/${user_id}`);
				setPosts(response.data);
			};

			fetchPosts();
		},
		[ user_id ]
	);

	return (
		<div>
			<h1>Posts by User {user_id}</h1>
			<div className="row g-3" style={{'padding':'25px'}}>
				{posts.map((post) => (
					<div className="col-md-4" key={post.id}>
						<PostCard post={post} />
					</div>
				))}
			</div>
		</div>
	);
};

export default Posts;
