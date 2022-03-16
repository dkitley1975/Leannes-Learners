const facebookBtn = document.querySelector('.facebook-btn');
const twitterBtn = document.querySelector('.twitter-btn');
const pinterestBtn = document.querySelector('.pinterest-btn');
const linkedinBtn = document.querySelector('.linkedin-btn');

function shareSocially() {
	const ShareImg = document.querySelector('.share-socially-img');

	let postUrl = encodeURI(document.location.href);
	let postTitle = encodeURI(
		'Hi everyone, thought I would share this brilliant article: '
	);
	let postImg = encodeURI(ShareImg.src);

	facebookBtn.setAttribute(
		'href',
		`https://www.facebook.com/sharer.php?u=${postUrl}`
	);

	twitterBtn.setAttribute(
		'href',
		`https://twitter.com/share?url=${postUrl}&text=${postTitle}&hashtags=leanneslearners, learntodrive, drivinglessons, femaledrivinginstructor, drivingschool, huddersfield`
	);

	pinterestBtn.setAttribute(
		'href',
		`https://pinterest.com/pin/create/bookmarklet/?media=${postImg}&url=${postUrl}&description=${postTitle}`
	);

	linkedinBtn.setAttribute(
		'href',
		`https://www.linkedin.com/shareArticle?url=${postUrl}&title=${postTitle}`
	);
}

shareSocially();
