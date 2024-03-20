import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Logs: React.FC = () => {
	const [ logs, setLogs ] = useState<any[]>([]);

	useEffect(() => {
		const fetchLogs = async () => {
			const response = await axios.get('http://localhost:8000/logs');
			setLogs(response.data);
		};

		fetchLogs();
	}, []);

	return (
		<div>
			<h1>Logs</h1>
			<div style={{ padding: '25px' }}>
				<table className="table table-striped table-hover table-borderless">
					<thead className="table-dark" style={{ textAlign: 'center' }}>
						<tr>
							<th>ID</th>
							<th>Timestamp</th>
							<th>Request Type</th>
							<th>Request URL</th>
							<th>Response Status</th>
						</tr>
					</thead>
					<tbody style={{ textAlign: 'center' }}>
						{logs
							.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime())
							.map((log) => (
								<tr key={log.id}>
									<td>{log.id}</td>
									<td>{new Date(log.timestamp).toLocaleString()}</td>
									<td>{log.request_type}</td>
									<td>{log.request_url}</td>
									<td>{log.response_status}</td>
								</tr>
							))}
					</tbody>
				</table>
			</div>
		</div>
	);
};

export default Logs;
