<script>
function showSearch() {
		searchForm = document.getElementById("search");
		searchForm.style.display = '';
		

		searchBtn = document.getElementById("searchBtn");
		searchBtn.removeAttribute('onclick');
		searchBtn.setAttribute('onclick', 'hideSearch()');
		searchBtn.children[0].classList.remove('fa-search');
		searchBtn.children[0].classList.add('fa-close');
	};

	function hideSearch() {
		searchForm = document.getElementById("search");
		searchForm.style.display = 'none';

		searchBtn = document.getElementById("searchBtn");
		searchBtn.removeAttribute('onclick');
		searchBtn.setAttribute('onclick', 'showSearch()');
		searchBtn.children[0].classList.remove('fa-close');
		searchBtn.children[0].classList.add('fa-search');
	};

	</script>