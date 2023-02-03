window.addEventListener("load", () => {
	getDescription('id_description');
	getName();
	getImage();
	getTags();
});

function getDescription(area_id){
	console.log('aa');
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

function getImage(){
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

// let tags_item = document.getElementById('tags-item').querySelector('input');
// tags_item.oninput = function(){
// 	let tags = [];
// 	for (let i = 0; i < tags_item.value.split(',').length; i++){
// 		let n = tags_item.value.split(',')[i].trim(' ');
// 		if(n){
// 			tags.push("#" + n);
// 		}
// 	}
// 	let tags_str = '';
// 	let t = Array.from(new Set(tags));
// 	for (let i = 0; i < t.length; i++) {
// 		tags_str += `<div class="s-tag">${t[i]}</div>`;
// 	}
// 	document.getElementById('section-tags').innerHTML = tags_str;
// }
