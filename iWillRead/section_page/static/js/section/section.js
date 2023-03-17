export function contentOperations(post_func){
	let f = null;
	if(post_func){
		f = post_func;
	}
	else{
		f = function(){}
	}
	getDescription('id_description');
	getName();
	getImage(f);
	getTags();
}

function getDescription(area_id){
	let select_area = tinymce.get(area_id);
	if(select_area.getContent() != ''){
		document.getElementById('section-text').innerHTML = select_area.getContent();
	}
	select_area.on('Paste Change input Undo Redo', function() {
		document.getElementById('section-text').innerHTML = select_area.getContent();
	});
}

function getName(){
	let input_name = document.getElementById('form-item-name').querySelector('input');
	if(input_name.value != ''){
		document.getElementById('section-path-name').innerHTML = input_name.value;
	}
	input_name.oninput = function(){
		document.getElementById('section-path-name').innerHTML = this.value;
	}
}

function getImage(post_func){
	let image = document.getElementById('form-item-image').querySelector('input');
	if(image.files[0]){
		let file = image.files[0];
		let new_img = document.createElement('img');
		new_img.src = URL.createObjectURL(file);
		document.getElementById('section-image-wrap').innerHTML = '';
		document.getElementById('section-image-wrap').appendChild(new_img);
	}
	image.onchange = function(){
		let file = this.files[0];
		let new_img = document.createElement('img');
		new_img.src = URL.createObjectURL(file);
		document.getElementById('section-image-wrap').innerHTML = '';
		document.getElementById('section-image-wrap').appendChild(new_img);
		setTimeout(() => {
			post_func();
		}, "200");
	}
}

function getTags(){
	let tags_item = document.getElementById('tags-item').querySelector('input');
	if(tags_item.value){
		let tags = [];
		for (let i = 0; i < tags_item.value.split(',').length; i++){
			let n = tags_item.value.split(',')[i].trim(' ');
			if(n){
				tags.push("#" + n);
			}
		}
		let tags_str = '';
		let t = Array.from(new Set(tags));
		for (let i = 0; i < t.length; i++) {
			tags_str += `<div class="s-tag">${t[i]}</div>`;
		}
		document.getElementById('section-tags').innerHTML = tags_str;
	}
	tags_item.oninput = function(){
		let tags = [];
		for (let i = 0; i < tags_item.value.split(',').length; i++){
			let n = tags_item.value.split(',')[i].trim(' ');
			if(n){
				tags.push("#" + n);
			}
		}
		let tags_str = '';
		let t = Array.from(new Set(tags));
		for (let i = 0; i < t.length; i++) {
			tags_str += `<div class="s-tag">${t[i]}</div>`;
		}
		document.getElementById('section-tags').innerHTML = tags_str;
	}
}

export function resizeLeftContent(section_top_id, section_image_id, section_left_content_id){
	let container_jeft_side = document.getElementById('container-jeft-side');
	let section_top = document.getElementById(section_top_id);
	let section_image = document.getElementById(section_image_id);
	let section_left_content = document.getElementById(section_left_content_id);

	let r = section_top.offsetHeight + section_image.offsetHeight;
	let content_h = container_jeft_side.offsetHeight - r;
	section_left_content.style.height = (content_h - 5) + 'px';
	console.log(section_image.offsetHeight);
}
