
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


		function showSideMenu() {
			document.getElementById('side-menu').style.width = '100%';
			document.body.style.overflow = 'hidden';
			
		}
		function hideSideMenu() {
			document.getElementById('side-menu').style.width = '0';
			document.body.style.overflow = '';
		}

		function showDropMenu(el) {

			ar = document.getElementById(el);

			if (ar.getAttribute('data-open') == 0) {
				
				
				

				dr = document.getElementById('dr' + ar.getAttribute('data-id'));
				dr.style.display = 'block';
				ar.setAttribute('data-open', '1')
				ar.style.color = 'var(--primary)';
				ar.style.transform = 'rotate(180deg)';
			} else {
				
				dr = document.getElementById('dr' + ar.getAttribute('data-id'));
				dr.style.display = 'none';
				ar.setAttribute('data-open', '0')
				ar.title = 0;
				ar.style.color = '';
				ar.style.transform = 'rotate(0deg)';

			}
		}
