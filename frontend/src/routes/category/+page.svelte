<script lang="ts">
	import { onMount } from "svelte";const 
	apiURL = 'http://127.0.0.1:8000/api/v1/manga/category';
	let data:any[]
	onMount(async function() {
		const response = await fetch(apiURL);
		data = await response.json();
		}
	);
</script>
<main>
	{#each data as item}
		<p>{item.User}</p>
	{/each}
</main>