<script lang="ts">
	import '../app.css';
	import { Button, DropdownMenu, NavigationMenu } from "bits-ui";
	import logo from "$lib/assets/logo2.webp";
	import {Modal} from "@skeletonlabs/skeleton-svelte";
	import CaretDown from "phosphor-svelte/lib/CaretDown";
	import cn from "clsx";

	let { children } = $props();
	let openState = $state(false);

	function modalClose() {
		openState = false;
	}

	type ListItemProps = {
		className?: string;
		title: string;
		href: string;
		content: string;
	};
</script>

{#snippet ListItem({ className, title, content, href }: ListItemProps)}
<li>
	<NavigationMenu.Link
		class={cn(
		"hover:bg-muted hover:text-accent-foreground focus:bg-muted focus:text-accent-foreground outline-hidden block select-none space-y-1 rounded-md p-3 leading-none no-underline transition-colors",
		className
		)}
		{href}
	>
		<div class="text-sm font-medium leading-none">{title}</div>
		<p class="text-muted-foreground line-clamp-2 text-sm leading-snug">
		{content}
		</p>
	</NavigationMenu.Link>
</li>
{/snippet}

<!-- component -->
<nav class="flex w-full justify-between px-10 py-4 items-center">
	<img src={logo} alt="komikSpace">
	<div class="flex items-center ">
		<ul class="flex items-center space-x-6 w-full">
			<li class="font-semibold text-gray-700"><a href="/">Home</a></li>
			<li class="font-semibold text-gray-700">
				<NavigationMenu.Root class="relative z-10 flex w-full justify-center">
					<NavigationMenu.List
						class="group flex list-none items-center justify-center p-1"
					>
						<NavigationMenu.Item value="category" openOnHover={false}>
							<NavigationMenu.Trigger
								class="hover:text-accent-foreground focus-visible:bg-muted focus-visible:text-accent-foreground data-[state=open]:shadow-mini dark:hover:bg-muted dark:data-[state=open]:bg-muted focus-visible:outline-hidden group inline-flex h-8 w-max items-center justify-center rounded-[7px] bg-transparent px-4 py-2 text-sm font-medium transition-colors hover:bg-white disabled:pointer-events-none disabled:opacity-50 data-[state=open]:bg-white"
							>
								Category
								<CaretDown
								class="relative top-[1px] ml-1 size-3 transition-transform duration-200 group-data-[state=open]:rotate-180"
								aria-hidden="true"
								/>
							</NavigationMenu.Trigger>
							<NavigationMenu.Content
								class="data-[motion=from-end]:animate-enter-from-right data-[motion=from-start]:animate-enter-from-left data-[motion=to-end]:animate-exit-to-right data-[motion=to-start]:animate-exit-to-left absolute left-0 top-0 w-full sm:w-auto"
							>
								<ul
								class="m-0 grid list-none gap-x-2.5 p-3 sm:w-[600px] sm:grid-flow-col sm:grid-rows-3 sm:p-[22px]"
								>
									<li class="row-span-3 mb-2 sm:mb-0">
										<NavigationMenu.Link
										href="/"
										class="from-muted/50 to-muted bg-linear-to-b outline-hidden flex h-full w-full select-none flex-col justify-end rounded-md p-6 no-underline focus:shadow-md"
										>
										<!-- <Icons.logo class="h-6 w-6" /> -->
										<div class="mb-2 mt-4 text-lg font-medium">Bits UI</div>
										<p class="text-muted-foreground text-sm leading-tight">
											The headless components for Svelte.
										</p>
										</NavigationMenu.Link>
									</li>
									{@render ListItem({
										href: "/category/manga",
										title: "Manga",
										content: "Japanese comic books and graphic novels with unique art style and storytelling"
									})}
									{@render ListItem({
										href: "/category/manhwa",
										title: "Manhwa",
										content: "Korean comics and webtoons known for their vibrant colors and vertical scrolling format"
									})}
									{@render ListItem({
										href: "/category/manhua",
										title: "Manhua",
										content: "Chinese comics featuring distinctive art styles and cultural themes"
									})}
								</ul>
							</NavigationMenu.Content>
						</NavigationMenu.Item>
						<NavigationMenu.Indicator
						class="data-[state=hidden]:animate-fade-out data-[state=visible]:animate-fade-in top-full z-10 flex h-2.5 items-end justify-center overflow-hidden opacity-100 transition-[all,transform_250ms_ease] duration-200 data-[state=hidden]:opacity-0"
						>
						<div
							class="bg-border relative top-[70%] size-2.5 rotate-[45deg] rounded-tl-[2px]"
						></div>
						</NavigationMenu.Indicator>
					</NavigationMenu.List>
					<div
						class="perspective-[2000px] absolute left-0 top-full flex w-full justify-center"
					>
						<NavigationMenu.Viewport
						class="text-popover-foreground bg-background data-[state=closed]:animate-scale-out data-[state=open]:animate-scale-in absolute mt-2.5 h-[var(--bits-navigation-menu-viewport-height)] w-full origin-[top_center] overflow-hidden rounded-md border shadow-lg transition-[width,_height] duration-200 sm:w-[var(--bits-navigation-menu-viewport-width)]"
						/>
					</div>
				</NavigationMenu.Root>
			</li>
			<li>
				<a href="/favorite">Favorite</a>
			</li>
		</ul>
	</div>
	<div>
		<Modal
			open={openState}
			onOpenChange={(e) => (openState = e.open)}
			contentBase="card bg-surface-100-900 p-4 space-y-4 shadow-xl max-w-screen-sm"
			backdropClasses="backdrop-blur-sm"
			>
			{#snippet trigger()}
				<Button.Root
				class="rounded-input bg-purple-600 text-white shadow-mini hover:bg-purple-700 inline-flex
					h-10 items-center justify-center px-[15px] text-[15px]
					font-semibold active:scale-[0.98] active:transition-all"
				>
				Masuk
				</Button.Root>
			{/snippet}
			{#snippet content()}
				<header class="flex justify-between">
					<h2 class="h2">Modal Example</h2>
				</header>
				<article>
					<p class="opacity-60">
						Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, ab adipisci. Libero cumque sunt quis error veritatis amet, expedita
						voluptatem. Quos repudiandae consequuntur voluptatem et dicta quas, reprehenderit velit excepturi?
					</p>
				</article>
				<footer class="flex justify-end gap-4">
					<button type="button" class="btn preset-tonal" onclick={modalClose}>Cancel</button>
					<button type="button" class="btn preset-filled" onclick={modalClose}>Confirm</button>
				</footer>
			{/snippet}
		</Modal>
	</div>
</nav>

{@render children()}
