from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="PatchedUpdateSkillSetRequest")



@_attrs_define
class PatchedUpdateSkillSetRequest:
    """ Update skill set metadata (name, description, key) only.

        Attributes:
            name (str | Unset):
            description (str | Unset):
            knowledge_base_key_id (None | Unset | UUID):
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    knowledge_base_key_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        knowledge_base_key_id: None | str | Unset
        if isinstance(self.knowledge_base_key_id, Unset):
            knowledge_base_key_id = UNSET
        elif isinstance(self.knowledge_base_key_id, UUID):
            knowledge_base_key_id = str(self.knowledge_base_key_id)
        else:
            knowledge_base_key_id = self.knowledge_base_key_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if knowledge_base_key_id is not UNSET:
            field_dict["knowledge_base_key_id"] = knowledge_base_key_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_knowledge_base_key_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_base_key_id_type_0 = UUID(data)



                return knowledge_base_key_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        knowledge_base_key_id = _parse_knowledge_base_key_id(d.pop("knowledge_base_key_id", UNSET))


        patched_update_skill_set_request = cls(
            name=name,
            description=description,
            knowledge_base_key_id=knowledge_base_key_id,
        )


        patched_update_skill_set_request.additional_properties = d
        return patched_update_skill_set_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
