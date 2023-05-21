/* -------------------------------------------------------------------------------- /
	
	Magentech jQuery
	Created by Magentech
	v1.0 - 20.9.2016
	All rights reserved.
	
/ -------------------------------------------------------------------------------- */

	// Cart add remove functions
	var cart = {
		'add': function(product_id, quantity) {
			addProductNotice('Ürün Sepete Eklendi', '<img src="/static/image/demo/shop/product/e11.jpg" alt="">', '<h3><a href="#">Ürün</a> sepetinize <a href="#">eklendi</a>!</h3>', 'success');
		}
	}

	var wishlist = {
		'add': function(product_id) {
			addProductNotice('Ürün istek listenize eklendi', '<img src="/static/image/demo/shop/product/e11.jpg" alt="">', '<h3>Önce <a href="#">giris</a>  yapmalısınız <a href="#">Ürünü"</a> to your <a href="#">istek listesine</a>!</h3>', 'success');
		}
	}
	var compare = {
		'add': function(product_id) {
			addProductNotice('Ürün karşılaştırmaya eklendi', '<img src="/static/image/demo/shop/product/e11.jpg" alt="">', '<h3>Başarılı: Ürün <a href="#">karşılaştırma"</a> listenize <a href="#">eklendi</a>!</h3>', 'success');
		}
	}

	/* ---------------------------------------------------
		jGrowl – jQuery alerts and message box
	-------------------------------------------------- */
	function addProductNotice(title, thumb, text, type) {
		$.jGrowl.defaults.closer = false;
		//Stop jGrowl
		//$.jGrowl.defaults.sticky = true;
		var tpl = thumb + '<h3>'+text+'</h3>';
		$.jGrowl(tpl, {		
			life: 4000,
			header: title,
			speed: 'slow',
			theme: type
		});
	}

